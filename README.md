❤️ Heart Disease Prediction
📌 Project Overview
This project focuses on predicting the presence of heart disease using machine learning models based on clinical and demographic patient features. The workflow includes data preprocessing, handling class imbalance, model optimization, evaluation, and comparison of multiple models.

🎯 Project Objective
The main goal is to build reliable classification models that can predict whether a patient has heart disease (1) or not (0) using structured medical data.

🔗 Live App
Try the App Now!

📊 Dataset
The dataset contains patient health information:
Feature	Description
Age	Patient age
Sex	Gender
ChestPainType	Type of chest pain
RestingBP	Resting blood pressure
Cholesterol	Serum cholesterol
FastingBS	Fasting blood sugar
RestingECG	Resting electrocardiographic results
MaxHR	Maximum heart rate achieved
ExerciseAngina	Exercise-induced angina
Oldpeak	ST depression induced by exercise
ST_Slope	ST segment slope during exercise

Target Variable:
0 → No heart disease
1 → Heart disease present

🔄 Project Workflow
📥 Data Loading & Inspection

↓

📊 Exploratory Data Analysis (EDA)

↓

🧹 Data Preprocessing

↓

✂️ Train-Test Split
✂️

↓

⚖️ Handling Class Imbalance (SMOTE)

↓

🏗️ Model Building with Pipelines

↓

🔧 Hyperparameter Tuning (RandomizedSearchCV)

↓

📈 Final Evaluation

↓

🎯 Feature Importance Analysis


🤖 Models Used
Model	Description
🌲 Random Forest Classifier	Ensemble tree-based method
⚡ XGBoost Classifier	Advanced gradient boosting
Both models were built using proper pipeline structure to prevent data leakage during resampling.


🛠️ Technologies & Tools
🐍 Python
📊 Pandas & NumPy - Data processing
📈 Matplotlib & Seaborn - Visualization
🔬 Scikit-learn - Machine learning
⚖️ Imbalanced-learn - SMOTE for class imbalance
🚀 XGBoost - Gradient boosting
☁️ Google Colab - Development environment
🌐 Streamlit - Web app deployment
deployment

📏 Evaluation Metrics
Since this is a medical classification problem, special attention was given to Recall and F1-Score:

✅ Accuracy
🎯 Precision
💡 Recall
⭐ F1-Score
📉 ROC-AUC

🏆 Key Results
Both models achieved strong performance on the test set
Random Forest was selected as the best model based on F1-Score and ROC-AUC
ST_Slope_Up and ST_Slope_Flat were the most important predictive features
Model comparison was performed to choose the optimal model

model
📁 Repository Structure
Heart-Disease-Prediction/

├── 📄 README.md # Project documentation

├── 📊 heart.csv # Dataset

├── 🧠 heart_disease_modeling.ipynb # Model development notebook

├── 🤖 heart_disease_final_model.pkl # Trained model

├── 🌐 app.py # Streamlit web app

├── 📦 requirements.txt # Dependencies

└── 📜 LICENSE # MIT License

How to Run Locally
https://github.com/Ali13fffff/Heart-Disease-Prediction2.git

⚠️ Disclaimer
Warning: This project is for educational and demonstration purposes only. For actual medical diagnosis, please consult a qualified healthcare professional.

👤 Author
Ali - Data Scientist / Developer

📜 License
MIT License

🎉 Thank You!
If you found this project helpful, please give it a ⭐ star!

🌐 Live App: https://heart-disease-prediction2-2vsziubidqx64ppfjzuwa6.streamlit.app/
Please use VPN to access this app.🖕🖕




