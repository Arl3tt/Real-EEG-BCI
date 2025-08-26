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

---

## ⚙️ Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/Arl3tt/Real-EEG-BCI.git
cd RealTimeBCI
pip install -r requirements.txt
