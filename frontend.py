import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Insurance Premium Predictor",
    layout="centered"
)

st.title("🏥 Insurance Premium Predictor")
st.markdown("Fill in your details below")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        value=65.0
    )

    height = st.number_input(
        "Height (m)",
        min_value=0.5,
        max_value=2.5,
        value=1.70
    )

    smoker = st.selectbox(
        "Smoker",
        [True, False]
    )

with col2:
    income_lpa = st.number_input(
        "Income (LPA)",
        min_value=0.1,
        value=10.0
    )

    city = st.text_input(
        "City",
        "Mumbai"
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job"
        ]
    )

if st.button("Predict Premium"):

    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "smoker": smoker,
        "city": city,
        "income_lpa": income_lpa,
        "occupation": occupation
    }

    try:
        res = requests.post(API_URL, json=payload)

        result = res.json()

        if res.status_code == 200:

            st.success("Prediction Successful")
            st.success(f"Predicted Category: {result['predicted_category']}")
           # st.write("### Prediction Result")
          #  st.write(result)

           # if "response" in result:
               # st.success(
                #    f"Predicted Premium: {result['response']}"
               # )

        else:
            st.error("Prediction Failed")
            st.json(result)

    except requests.exceptions.ConnectionError:
        st.error(
            "❌ FastAPI server is not running.\n\n"
            "Start backend first:\n"
            "uvicorn main:app --reload"
        )