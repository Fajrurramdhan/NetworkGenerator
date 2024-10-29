import streamlit as st


option = st.selectbox(
    "Risk Value",
    ("Tsunami", "Gempa Bumi", "Tanah Longsor"),
    index=None,
    placeholder="Select contact method...",
)

st.write("You selected:", option)