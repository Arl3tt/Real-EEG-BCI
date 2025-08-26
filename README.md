# Real-EEG-BCI 🧠 

This project implements a **real-time Brain-Computer Interface (BCI) data acquisition and feature extraction pipeline** for EEG-based neurofeedback.  
It streams EEG signals (from **LSL/OpenBCI**) or simulates them if no device is connected, then computes **band power features (theta, alpha, beta)** for cognitive monitoring and neurofeedback applications.

---

## 🚀 Features
- Connects to **live EEG streams** via [Lab Streaming Layer (LSL)](https://github.com/sccn/labstreaminglayer).
- Falls back to **simulated EEG data** if no device is detected.
- Saves raw EEG signals to CSV (`Real-EEG-BCI_raw.csv`).
- Extracts **theta, alpha, and beta band powers** and saves them as:
  - CSV (`Real-EEG-BCI.csv`)
  - JSON (`Real-EEG-BCI_features.json`) for real-time feedback loops.
- Reproducible simulations using fixed random seeds.

---

## Dependencies:

numpy

pandas

scipy

pylsl (for real EEG streaming, optional)

## ▶️ Usage

Run the script to fetch EEG data (from real device if available, otherwise simulated):

python "Real-Time BCI.py"


Or import the function into your own project:

from real_time_bci import fetch_mindbalance_data

df = fetch_mindbalance_data(eeg_channels=8, sample_rate=256, duration_sec=5)
print(df.head())

## 📊 Outputs

After running, the following files will be created in the data/ folder:

mindbalance_raw.csv → raw EEG time series.

mindbalance_features.csv → computed band power features.

mindbalance_features.json → JSON records for web/real-time apps.

## 🧠 Tech Stack

Python (NumPy, Pandas, SciPy)

pylsl for EEG streaming (optional)

Supports OpenBCI and other LSL-compatible EEG devices

## 📈 Roadmap

 Add real-time WebSocket streaming of features

 Build interactive neurofeedback dashboard (React + TensorFlow.js)

 Expand feature set (gamma, delta bands, connectivity measures)
---
## 📂 Project Structure
```bash
RealTimeBCI/
│── Real-Time BCI.py         # Main Python script (EEG fetch + feature extraction)
│── README.md                # Documentation for GitHub
│── requirements.txt         # Dependencies list
│── data/                    # Auto-created folder (saves EEG raw + feature files)
│    ├── mindbalance_raw.csv
│    ├── mindbalance_features.csv
│    └── mindbalance_features.json
│── .gitignore               # Ignore cache, data, venv files (optional)

## ⚙️ Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/Arl3tt/Real-EEG-BCI.git
cd RealTimeBCI
pip install -r requirements.txt
