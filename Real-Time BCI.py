import os
import json
import time
import pandas as pd
import numpy as np
from datetime import datetime
from scipy.signal import welch

try:
    from pylsl import StreamInlet, resolve_stream
except ImportError:
    StreamInlet = None

def fetch_mindbalance_data(
    eeg_channels=8,
    sample_rate=256,
    duration_sec=10
):
    """
    Fetch EEG data and extract band power features for neurofeedback.
    """
    os.makedirs("data", exist_ok=True)

    eeg_data = []
    timestamps = []

    if StreamInlet:
        try:
            print("[MindBalance] Searching for LSL EEG stream...")
            streams = resolve_stream('type', 'EEG')
            inlet = StreamInlet(streams[0])
            print("[MindBalance] Connected! Streaming data...")
            start_time = time.time()
            while time.time() - start_time < duration_sec:
                sample, ts = inlet.pull_sample(timeout=1.0)
                if sample:
                    eeg_data.append(sample)
                    timestamps.append(ts)
        except Exception as e:
            print(f"[MindBalance] No live stream found, simulating data... ({e})")
            eeg_data, timestamps = simulate_eeg(eeg_channels, sample_rate, duration_sec)
    else:
        print("[MindBalance] pylsl not installed — simulating EEG data.")
        eeg_data, timestamps = simulate_eeg(eeg_channels, sample_rate, duration_sec)

    eeg_df = pd.DataFrame(eeg_data, columns=[f"ch{i+1}" for i in range(eeg_channels)])
    eeg_df["timestamp"] = timestamps
    raw_path = "data/mindbalance_raw.csv"
    eeg_df.to_csv(raw_path, index=False)
    print(f"[MindBalance] Raw data saved to {raw_path}")

    # Compute band powers
    band_features = compute_band_powers(np.array(eeg_data), sample_rate)
    feature_df = pd.DataFrame(band_features)
    feature_df["timestamp"] = timestamps[:len(feature_df)]
    feat_path = "data/mindbalance_features.csv"
    feature_df.to_csv(feat_path, index=False)
    print(f"[MindBalance] Features saved to {feat_path}")

    # Save JSON for real-time feedback
    json_path = "data/mindbalance_features.json"
    with open(json_path, "w") as f:
        json.dump(feature_df.to_dict(orient="records"), f)
    print(f"[MindBalance] JSON features saved to {json_path}")

    return feature_df

def compute_band_powers(data, fs):
    """
    Compute alpha, beta, theta power bands.
    """
    bands = {
        "theta": (4, 8),
        "alpha": (8, 13),
        "beta": (13, 30)
    }
    features = []
    for ch in data.T:
        f, psd = welch(ch, fs=fs, nperseg=fs*2)
        ch_feats = {}
        for band, (low, high) in bands.items():
            idx = np.logical_and(f >= low, f <= high)
            ch_feats[band] = np.mean(psd[idx])
        features.append(ch_feats)
    return features

def simulate_eeg(channels, rate, duration):
    total_samples = rate * duration
    rng = np.random.default_rng(seed=42)  # Create a Generator instance with a fixed seed
    data = rng.standard_normal((total_samples, channels))  # Use Generator method
    ts = [datetime.now().timestamp() + i/rate for i in range(total_samples)]
    return data, ts

# Example run:
# fetch_mindbalance_data(eeg_channels=8, sample_rate=256, duration_sec=5)