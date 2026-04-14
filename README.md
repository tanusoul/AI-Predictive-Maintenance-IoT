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

## 🏗️ Project Architecture
IoT Sensors → Data Collection → Data Preprocessing →
Feature Engineering → Machine Learning Model →
Failure Prediction → Visualization → Maintenance Decision

---

## 📂 Project Structure
AI-Predictive-Maintenance-IoT/
│
├── data/
│ └── raw/
├── docs/
├── images/
│ └── confusion_matrix.png
├── models/
│ └── predictive_maintenance_model.pkl
├── notebooks/
├── outputs/
│ └── predictions.csv
├── src/
│ ├── data_preprocessing.py
│ ├── train_model.py
│ ├── evaluate_model.py
│ ├── predict.py
│ └── visualize.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/tanusoul/AI-Predictive-Maintenance-IoT.git
cd AI-Predictive-Maintenance-IoT
2️⃣ Create a Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Project
python main.py
📈 Model Performance

The Random Forest model achieves high accuracy in predicting machine failures using simulated IoT sensor data.

Evaluation Metrics:

Accuracy
Precision
Recall
F1-Score
Confusion Matrix

🔮 Future Enhancements
Real-time IoT data integration using MQTT
Deployment with Streamlit or Flask
Deep Learning models such as LSTM
Cloud deployment using AWS or Azure
Integration with Power BI dashboards
Edge AI deployment for smart factories
🎓 Learning Outcomes
Predictive Maintenance using Artificial Intelligence
Industrial IoT Analytics
End-to-End Machine Learning Pipeline
Data Preprocessing and Feature Engineering
Model Evaluation and Visualization
Version Control with Git and GitHub
👩‍💻 Author

Tanuja
B.Tech in Computer Science Engineering (AI & ML)

📜 License

This project is intended for educational and portfolio purposes.

⭐ Acknowledgements
UCI Machine Learning Repository
AI4I Predictive Maintenance Dataset
Scikit-learn Documentation
Open-source AI community