pip install streamlit
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

st.title("🩺 Symptom Checker Bot")
user_input = st.text_input("Describe your symptoms:")

if user_input:
    tokens = word_tokenize(user_input.lower())
    symptom_map = load_symptom_data()
    matched_conditions = set()

    for token in tokens:
        if token in symptom_map:
            matched_conditions.update(symptom_map[token])

    if matched_conditions:
        st.subheader("Possible Conditions:")
        for condition in matched_conditions:
            st.write(f"- {condition}")
        st.info("This is not a diagnosis. Please consult a healthcare professional.")
    else:
        st.warning("No matches found. Try rephrasing your symptoms.")
