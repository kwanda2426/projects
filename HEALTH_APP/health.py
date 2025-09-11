import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
dt_model = joblib.load("decision_tree_model.pkl")

# Encoding dictionaries
gender_dict = {'M': 1, 'F': 0}
BP_dict = {'HIGH': 2, 'NORMAL': 0, 'LOW': 1}
Chol_dict = {'HIGH': 1, 'NORMAL': 0}
reverse_drug_dict = {4: 'DrugY', 3: 'drugX', 2: 'drugA', 1: 'drugC', 0: 'drugB'}

st.title("Drug Prediction App 💊")

# --- Dataset selection ---
st.subheader("Load dataset")
url = "https://raw.githubusercontent.com/kwanda2426/projects/main/drug_data.csv"

option = st.radio(
    "Choose how to load data:",
    ("Use default dataset (GitHub)", "Upload your own file")
)

required_cols = ["Age", "Sex", "BP", "Cholesterol", "Na_to_K", "Drug"]

if option == "Use default dataset (GitHub)":
    df = pd.read_csv(url)
    st.success("Loaded dataset from GitHub ✅")
else:
    uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Check required columns
        if all(col in df.columns for col in required_cols):
            st.success("Loaded your uploaded dataset ✅")
        else:
            st.error(f"❌ File must contain these columns: {required_cols}")
            st.stop()
    else:
        st.warning("Please upload a file to continue.")
        st.stop()

st.dataframe(df.head())  # preview first rows

# --- Prediction section ---
st.subheader("Make a prediction")

age = st.number_input("Age", min_value=0, max_value=100, value=30)
sex = st.selectbox("Sex", ["M", "F"])
bp = st.selectbox("Blood Pressure", ["HIGH", "NORMAL", "LOW"])
chol = st.selectbox("Cholesterol", ["HIGH", "NORMAL"])
na_to_k = st.number_input("Na_to_K Ratio", value=15.0)

# Encode
sex_enc = gender_dict[sex]
bp_enc = BP_dict[bp]
chol_enc = Chol_dict[chol]

if st.button("Predict Drug"):
    features = np.array([[age, sex_enc, bp_enc, chol_enc, na_to_k]])
    prediction = dt_model.predict(features)[0]
    st.success(f"Predicted Drug: {reverse_drug_dict[prediction]}")
