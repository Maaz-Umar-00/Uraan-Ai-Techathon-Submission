import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# Page config
st.set_page_config(page_title="PSDP Insight AI", layout="wide")


# ---- Load Model and Feature Columns ----
APP_DIR = Path(__file__).resolve().parent


@st.cache_resource
def load_model_and_features(model_path: Path, features_path: Path):
    # Load with explicit paths so relative locations work when deployed
    loaded_model = joblib.load(model_path)
    loaded_features = joblib.load(features_path)
    return loaded_model, loaded_features


try:
    model_file = APP_DIR / "psdp_efficiency_model.pkl"
    features_file = APP_DIR / "model_features.pkl"
    model, model_features = load_model_and_features(model_file, features_file)
except Exception as e:
    st.error("Failed to load model or feature list. Make sure the `.pkl` files are present in the app folder.")
    st.exception(e)
    st.stop()


st.title("📊 PSDP Insight AI — Project Efficiency Predictor")
st.markdown("Enter project details below to predict efficiency 👇")

# ---- User Input Form ----
with st.form("project_form"):
    total_cost = st.number_input("💰 Total Project Cost (in million Rs)", min_value=0.0, value=1000.0)
    expenditure = st.number_input("💸 Expenditure 2024 (in million Rs)", min_value=0.0, value=600.0)
    foreign_loan = st.number_input("🌍 Foreign Loan (in million Rs)", min_value=0.0, value=0.0)
    throwforward = st.number_input("↩️ Throwforward 2025", min_value=0.0, value=200.0)
    rupee_funding = st.number_input("💵 Rupee Funding", min_value=0.0, value=200.0)
    allocation = st.number_input("📦 Allocation 2024-25", min_value=0.0, value=300.0)
    year = st.number_input("📅 Approval Year", min_value=2000, max_value=2025, value=2022)
    
    ministry = st.selectbox("🏢 Ministry", [
        "FINANCE DIVISION", "HEALTH DIVISION", "EDUCATION DIVISION",
        "WATER RESOURCES", "PLANNING DEVELOPMENT", "OTHER"
    ])
    proj_type = st.selectbox("📂 Project Type", ["On-going", "New"])
    
    submitted = st.form_submit_button("🔮 Predict")

if submitted:
    # ---- Prepare Input ----
    new_data = pd.DataFrame([{
        "Total_Cost": total_cost,
        "Expenditure_2024": expenditure,
        "Foreign Loan": foreign_loan,
        "Throwforward_2025": throwforward,
        "Rupee_Funding": rupee_funding,
        "Allocation_2024_25": allocation,
        "Approval_Year": year,
        "Ministry": ministry,
        "Type": proj_type
    }])

    # ---- Encode and Align ----
    encoded_new = pd.get_dummies(new_data, columns=["Ministry", "Type"], drop_first=True)
    for col in model_features:
        if col not in encoded_new.columns:
            encoded_new[col] = 0
    encoded_new = encoded_new[model_features]

    # ---- Predict ----
    try:
        prediction = model.predict(encoded_new)[0]
    except Exception as e:
        st.error("Prediction failed. Check that the model supports .predict on the provided input shape.")
        st.exception(e)
        st.stop()

    # Some models may not have predict_proba; handle gracefully
    if hasattr(model, "predict_proba"):
        confidence = model.predict_proba(encoded_new)[0]
    else:
        # Fallback: if model only provides decision_function or raw output
        confidence = [None, None]

    # ---- Display Results ----
    if prediction == 1:
        if confidence[1] is not None:
            st.success(f"✅ Predicted: **Efficient Project** ({confidence[1]*100:.1f}% confidence)")
        else:
            st.success("✅ Predicted: **Efficient Project**")
    else:
        if confidence[0] is not None:
            st.error(f"⚠️ Predicted: **Inefficient Project** ({confidence[0]*100:.1f}% confidence)")
        else:
            st.error("⚠️ Predicted: **Inefficient Project**")

    # Optional: Show radar / bar of probabilities
    st.write("### Prediction Details")
    if confidence[1] is not None:
        st.metric("Efficiency Probability (%)", f"{confidence[1]*100:.2f}")
    if confidence[0] is not None:
        st.metric("Inefficiency Probability (%)", f"{confidence[0]*100:.2f}")
