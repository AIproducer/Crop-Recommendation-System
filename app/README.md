# 🌾 Crop Recommendation System

A Machine Learning web application that recommends the most suitable crop based on soil nutrients and environmental conditions.

---

## 📌 Features

- 🌱 Predicts the best crop using Machine Learning
- 📊 Random Forest Classifier (99.55% Accuracy)
- 📈 Feature Importance Visualization
- 📉 Confusion Matrix
- 🌾 Crop Images
- 🌍 Crop Information
- 📄 Download Prediction Report
- 💻 Interactive Streamlit Dashboard

---

## 🖥️ Demo

(Add a screenshot here)

---

## 📂 Project Structure

```text
Crop_Recommendation_System/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── tune_model.py
│   ├── evaluate.py
│   ├── predict.py
│   ├── utils.py
│   └── model_info.py
│
├── models/
│   └── crop_model.pkl
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
│
├── notebooks/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Dataset

- Total Samples: **2200**
- Features: **7**
- Crop Classes: **22**

### Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

---

## 🤖 Machine Learning Models Compared

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | 94.77% |
| Decision Tree | 97.95% |
| Random Forest | **99.55%** |
| KNN | 97.73% |
| SVM | 98.41% |
| Gradient Boosting | 98.86% |
| Extra Trees | 99.55% |

---

## 🛠 Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Joblib

---

## 🚀 Installation

```bash
git clone <your-repository-url>

cd Crop_Recommendation_System

pip install -r requirements.txt

streamlit run app/streamlit_app.py
```

---

## 👨‍💻 Developer

**Muhammad Ishfaq**

- Data Scientist
- Machine Learning Engineer