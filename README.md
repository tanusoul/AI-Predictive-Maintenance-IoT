# 🔧 AI-Powered Predictive Maintenance System for IoT Devices

## 📌 Overview
This project leverages Artificial Intelligence and Machine Learning to predict machine failures using IoT sensor data. It simulates real-world industrial predictive maintenance systems, enabling proactive decision-making and reducing downtime.

## 🎯 Problem Statement
Traditional maintenance strategies are either reactive or scheduled, leading to unexpected failures and increased operational costs. This project introduces a predictive approach that forecasts equipment failures before they occur.

## 🏭 Industry Applications
- Manufacturing Plants
- Automotive Industry
- Power Plants
- Aviation and Aerospace
- Smart Factories (Industry 4.0)
- Industrial IoT (IIoT)

## 🧠 Features
- Data preprocessing and feature engineering
- Machine failure prediction using Machine Learning
- Model evaluation with performance metrics
- Confusion matrix visualization
- Virtual simulation using real-world datasets
- Modular and scalable code structure
- GitHub-ready and industry-aligned implementation

## 🛠️ Tech Stack
| Category | Tools & Technologies |
|----------|----------------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Model Persistence | Joblib |
| Version Control | Git & GitHub |
| Development Environment | VS Code |
| Dataset | AI4I 2020 Predictive Maintenance Dataset |

## 📊 Dataset
**AI4I 2020 Predictive Maintenance Dataset**

It includes simulated IoT sensor data such as:
- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear

Target Variable:
- **Machine Failure (0 = No Failure, 1 = Failure)**

## 🏗️ System Architecture

1. **IoT Sensors**
2. **Data Collection**
3. **Data Storage**
4. **Data Preprocessing**
5. **Feature Engineering**
6. **Machine Learning Model**
7. **Failure Prediction**
8. **Visualization Dashboard**
9. **Maintenance Decision & Alerts**

---

## 📁 Project Structure

```text
AI-Predictive-Maintenance-IoT/
├── data/
│   └── raw/
├── docs/
├── images/
│   └── confusion_matrix.png
├── models/
│   └── predictive_maintenance_model.pkl
├── notebooks/
├── outputs/
│   └── predictions.csv
├── src/
│   ├── data_preprocessing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   ├── predict.py
│   └── visualize.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

