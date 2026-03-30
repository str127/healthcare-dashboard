import streamlit as st
from load_data import load_data
from analysis import advanced_analysis
from ml_model import train_model

st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

st.title("🏥 Healthcare Data Dashboard")

# Load data
patients_df, heart_df = load_data()

# Combine data
combined_df = advanced_analysis(patients_df, heart_df)

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔍 Filters")

selected_service = st.sidebar.selectbox(
    "Select Service",
    combined_df['service'].unique()
)

selected_target = st.sidebar.selectbox(
    "Heart Disease (0 = No, 1 = Yes)",
    [0, 1]
)

filtered_df = combined_df[
    (combined_df['service'] == selected_service) &
    (combined_df['target'] == selected_target)
]

# -------------------------------
# METRICS
# -------------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Patients", len(patients_df))
col2.metric("Avg Age", round(patients_df['age'].mean(), 2))
col3.metric("Heart Disease %", round(heart_df['target'].mean() * 100, 2))

# -------------------------------
# CHARTS
# -------------------------------

st.subheader(f"📈 Satisfaction for {selected_service} (Target = {selected_target})")

if not filtered_df.empty:
    st.bar_chart(filtered_df.groupby('service')['satisfaction'].mean())
else:
    st.warning("No data for selected filters")

st.subheader("📊 Age Distribution")
st.line_chart(patients_df['age'])

st.subheader("❤️ Heart Disease vs Satisfaction")
st.bar_chart(combined_df.groupby('target')['satisfaction'].mean())

# -------------------------------
# ML MODEL
# -------------------------------
st.subheader("🤖 Heart Disease Prediction")

model, accuracy = train_model(combined_df)

st.write(f"Model Accuracy: {round(accuracy*100, 2)}%")

age = st.slider("Age", 1, 100, 30)
trestbps = st.slider("Resting Blood Pressure", 80, 200, 120)
chol = st.slider("Cholesterol", 100, 400, 200)
thalach = st.slider("Max Heart Rate", 60, 220, 150)

prediction = model.predict([[age, trestbps, chol, thalach]])

if prediction[0] == 1:
    st.error("⚠️ High Risk of Heart Disease")
else:
    st.success("✅ Low Risk of Heart Disease")

# -------------------------------
# DATA VIEW
# -------------------------------
st.subheader("📋 Sample Data")
st.dataframe(combined_df.head(20))