"""Home page shown when the user enters the application"""
import streamlit as st

# pylint: disable=line-too-long
def app():
    with st.spinner("Loading Home ..."):
        st.write( "hello world, i should be home")
