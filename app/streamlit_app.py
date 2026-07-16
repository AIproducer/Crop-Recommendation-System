import streamlit as st
from src.predict import predict_crop
from src.utils import crop_info
import os
from src.model_info import MODEL_INFO

def load_css():
    css_path = os.path.join(
        os.path.dirname(__file__),
        "style.css"
    )

    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------------
# Sidebar (Paste Here)
# -----------------------------------

st.sidebar.metric(
    "Accuracy",
    MODEL_INFO["Accuracy"]
)

st.sidebar.metric(
    "Crop Classes",
    MODEL_INFO["Classes"]
)

st.sidebar.metric(
    "Features",
    MODEL_INFO["Features"]
)

st.sidebar.metric(
    "Dataset",
    MODEL_INFO["Dataset"]
)

st.sidebar.write("---")

st.sidebar.success(
    f"Model: {MODEL_INFO['Algorithm']}"
)

st.sidebar.write("👨‍💻 Muhammad Ishfaq")
# -----------------------------------
# Main Page
# -----------------------------------
tab1, tab2, tab3 = st.tabs(
    [
        "🌾 Prediction",
        "📊 Model Analysis",
        "ℹ About"
    ]
)

with tab1:
    st.markdown("""
# 🌾 Crop Recommendation System

### AI-powered recommendation using Machine Learning
""")

    st.write(
        "Enter soil nutrients and weather information to predict the most suitable crop."
    )

    col1, col2 = st.columns(2)

    with col1:

        N = st.slider("Nitrogen",0,140,90)

        P = st.slider("Phosphorus",5,145,42)

        K = st.slider("Potassium",5,205,43)

        temperature = st.number_input(
            "Temperature (°C)",
            0.0,
            50.0,
            20.8
        )

    with col2:

        humidity = st.number_input(
            "Humidity (%)",
            0.0,
            100.0,
            82.0
        )

        ph = st.number_input(
            "Soil pH",
            0.0,
            14.0,
            6.5
        )

        rainfall = st.number_input(
            "Rainfall (mm)",
            0.0,
            400.0,
            202.0
        )
    st.markdown("---")
    st.markdown("## 🎯 Prediction Result")
    if st.button("🌾 Predict Crop", use_container_width=True):

        crop, confidence = predict_crop(
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        )

        st.success(f"🌾 Recommended Crop: **{crop.upper()}**")

        st.metric(
            "Prediction Confidence",
            f"{confidence:.2f}%"
        )
        # --------------------------
        # Crop Image
        # --------------------------
    

        image_path = os.path.join(
            "images",
            "crops",
            f"{crop.lower()}.jpg"
            )
    

        if os.path.exists(image_path):
            st.image(
            image_path,
                width=350,
                caption=crop.capitalize()
            )
        else:
            st.warning(f"Image not found: {image_path}")
        from src.utils import crop_info

        if crop.lower() in crop_info:

            info = crop_info[crop.lower()]

            st.subheader("Crop Information")

            st.write(f"🌱 Season : {info['Season']}")
            st.write(f"🌍 Soil : {info['Soil']}")
            st.write(f"💧 Water : {info['Water']}")
            st.write(f"⏳ Duration : {info['Duration']}")

with tab2:

    st.header("📊 Model Performance")

    st.markdown("### Feature Importance")
    st.write("This chart shows how much each feature contributes to the prediction.")

    st.image(
        "images/feature_importance.png",
        use_container_width=True
    )

    st.markdown("### Confusion Matrix")
    st.write("The confusion matrix summarizes the model's classification performance.")

    st.image(
        "images/confusion_matrix.png",
        use_container_width=True
    )
with tab3:

    st.header("ℹ About This Project")

    st.markdown("""
### 🌱 Project

Machine Learning based Crop Recommendation System.

### 📊 Dataset

- 2200 Samples
- 22 Crop Classes
- 7 Features

### 🤖 Machine Learning Model

- Random Forest Classifier
- Accuracy: 99.55%

### 🛠 Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

### 👨‍💻 Developer

Muhammad Ishfaq
""")
    
st.write("---")

st.caption(
    "© 2026 Muhammad Ishfaq | Crop Recommendation System | Powered by Streamlit & Scikit-learn"
)