from multiapp import MultiApp
from src.pages import about, home, new_test, current_test, previous_test
import streamlit as st
import os
os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
apptitle = 'GW Quickview'

#needed to ensure that the same title is in every page and icon
st.set_page_config(page_title ="DAQ Demo",
                    initial_sidebar_state="collapsed",
                    page_icon="🔮")


app = MultiApp()
print("hello world")
# Add all your application here
app.add_app("New Test", new_test.app)
app.add_app("Home", home.app)
app.add_app("About", about.app)

app.add_app("Current Test", current_test.app)
app.add_app("Previous Test", previous_test.app)


# The main app
app.run()