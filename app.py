import streamlit as st


# Set page title and layout
st.set_page_config(page_title="Integrate Module Network Generation", layout="wide")


# Title
st.title("Integrate Module Network Generation")


# Layout with two main columns
col1, col2 = st.columns([2, 3])


# Left column (Input Data)
with col1:
    st.header("Input Data")
   
    # Base Area (Province) selection
    base_area = st.selectbox("Base Area (Province)", ["Select"] + ["Province A", "Province B", "Province C"])
   
    # Directory Name input
    directory_name = st.text_input("Directory Name")
   
    # Master Files Tabs
    st.subheader("Master Files")
    tab1, tab2 = st.tabs(["Locations", "Settings"])
   
    with tab1:
        st.markdown("**Master Locations (Point Of Interest)**")
        st.button("View Input")


# Right column (Execute Process)
with col2:
    st.header("Execute Process")
   
    # Directory Input, Output, and Status File Input
    directory_input = st.text_input("Directory Input", "not created yet", disabled=True)
    directory_output = st.text_input("Directory Output", "not created yet", disabled=True)
    status_file_input = st.text_input("Status File Input", "not provided yet", disabled=True)
   
    # Command Console
    st.markdown("**Command Console**")
    st.warning("Empty the command")
    command = st.text_input("Command Console", "python main.py directory_name/sample_input.json")
    st.button("Execute Command")
   
    # Console Status
    st.markdown("**Console Status**")
    st.empty()  # Placeholder for console status messages


# Additional guide button
st.button("Need Guide?", key="guide_button")