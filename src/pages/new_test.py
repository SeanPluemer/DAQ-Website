import streamlit as st
import src.test_configs
import csv_manipulation

def app():
    with st.spinner("Loading  ..."):

        st.write("I should be here")

        # Title the app
        st.title('DAQ Import Config')

        st.markdown("""
         * This is where you will configure new tests 
        """)
        st.subheader('1. Test config setup 🏋️')
        st.write("Import the configuration das file.")
        test_config_selection = st.selectbox("Select the test config file", ("new config" , "1", "2"))
