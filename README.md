# 🌾 Crop Recommendation System

<div align="center">

### An End-to-End Machine Learning Web Application for Intelligent Crop Recommendation

Predict the most suitable crop based on soil nutrients and environmental conditions using Machine Learning and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

---

# 📌 Project Overview

Agriculture plays a vital role in food production. Selecting the right crop based on soil composition and climatic conditions can significantly improve crop yield and reduce farming risks.

This project uses **Machine Learning** to recommend the most suitable crop based on:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

The application is deployed using **Streamlit** with an interactive and mobile-friendly interface.

---

# 🚀 Features

- 🌱 Predicts the best crop instantly
- 🤖 Random Forest Machine Learning Model
- 📊 Model comparison with multiple algorithms
- 📈 Feature Importance visualization
- 📉 Confusion Matrix
- 🌾 Crop images
- 📖 Crop information
- 🎨 Responsive Streamlit UI
- 📱 Mobile Friendly
- 💾 Pre-trained model support

---

# 📊 Dataset Information

| Property | Value |
|-----------|--------|
| Dataset Size | 2200 Samples |
| Crop Classes | 22 |
| Features | 7 |
| Target | Crop Name |

### Input Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

---

# 🌾 Supported Crops

- Apple
- Banana
- Blackgram
- Chickpea
- Coconut
- Coffee
- Cotton
- Grapes
- Jute
- Kidney Beans
- Lentil
- Maize
- Mango
- Moth Beans
- Mung Bean
- Muskmelon
- Orange
- Papaya
- Pigeon Peas
- Pomegranate
- Rice
- Watermelon

---

# 🧠 Machine Learning Models

The following algorithms were trained and evaluated.

| Model | Accuracy |
|--------|----------|
| Random Forest | **99.55%** ⭐ |
| Extra Trees | 99.55% |
| Gradient Boosting | 98.86% |
| SVM | 98.41% |
| Decision Tree | 97.95% |
| KNN | 97.73% |
| Logistic Regression | 94.77% |

**Best Model:** Random Forest Classifier

---

# 📂 Project Structure

```text
Crop-Recommendation-System
│
├── app/
│   ├── streamlit_app.py
│   └── style.css
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
│   ├── crops/
│   ├── confusion_matrix.png
│   └── feature_importance.png
│
├── models/
│   └── crop_model.pkl
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── EDA_2.ipynb
│   └── Preprocessing.ipynb
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
├── tests/
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/AIproducer/Crop-Recommendation-System.git
```

Move into the project

```bash
cd Crop-Recommendation-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app/streamlit_app.py
```

The application will be available at:

```
http://localhost:8501
```

---

# 📈 Model Evaluation

The Random Forest model achieved excellent performance:

- Accuracy: **99.55%**
- Precision: High
- Recall: High
- F1 Score: High

The project also includes:

- Cross Validation
- Hyperparameter Tuning (GridSearchCV)
- Feature Importance Analysis
- Confusion Matrix
- Classification Report

---

# 📸 Application Screenshots

## Home Page

> Add your homepage screenshot here.

```
images/home.png
```

---

## Prediction Result

> Add your prediction screenshot here.

```
images/prediction.png
```

---

## Feature Importance

```
images/feature_importance.png
```

---

## Confusion Matrix

```
images/confusion_matrix.png
```

---

# 🛠 Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib

### Web Framework

- Streamlit

### Model Storage

- Joblib

### Version Control

- Git
- GitHub

---

# 📈 Future Improvements

- Soil health analysis
- Fertilizer recommendation
- Weather API integration
- Disease prediction
- Crop yield estimation
- Multi-language support
- GPS-based recommendation

---

# 👨‍💻 Author

**Muhammad Ishfaq**

- Data Scientist
- Machine Learning Engineer
- Python Developer

GitHub:
https://github.com/AIproducer

LinkedIn:
(Add your LinkedIn profile)

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### 🌾 Happy Farming with Machine Learning 🌾

</div>
