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

## 📂 Project Structure
RealTimeBCI/
│── Real-Time BCI.py         # Main Python script (EEG fetch + feature extraction)
│── README.md                # Documentation for GitHub
│── requirements.txt         # Dependencies list
│── data/                    # Auto-created folder (saves EEG raw + feature files)
│    ├── mindbalance_raw.csv
│    ├── mindbalance_features.csv
│    └── mindbalance_features.json
│── .gitignore               # Ignore cache, data, venv files (optional)
