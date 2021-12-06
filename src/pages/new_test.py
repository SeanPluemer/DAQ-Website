import time

import streamlit as st
import src.test_configs
import csv_manipulation
import os
import csv
import pandas as pd

os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
#print(os.getcwd())
def import_test_config(csv_file_name):

    homepath = "/Users/seanpluemer/Documents/GitHub/DAQ-Website"
    os.chdir(homepath)
    time.sleep(1)
    path = "src/test_configs"
    os.chdir(path)
    if csv_file_name == "New Config":
            csv_file_name = "BlankTestConfigTemplate.csv"
    if csv_file_name == "1":
            csv_file_name = "Demo1TestConfigTemplate.csv"


    dict_from_csv = pd.read_csv(csv_file_name, header=None, index_col=0, squeeze=True).to_dict()
    print(dict_from_csv)





    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_of_column_names = []
        for row in csv_reader:
            list_of_column_names.append(row)
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    return dict_from_csv

def app():
    print(os.getcwd())
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    with st.spinner("Loading  ..."):

        st.write("I should be here")

        # Title the app
        st.title('DAQ Import Config')

        st.markdown("""
         * This is where you will configure new tests 
        """)
        st.subheader('1. Test config setup 🏋️')
        st.write("Import the configuration das file.")
        test_config_selection_name = st.selectbox("Select the test config file", ("New Config" , "1", "2"))
        if test_config_selection_name=="New Config":
            st.write(test_config_selection_name)
            title = st.text_input('Movie title', 'Life of Brian')
            test_config_selection_data = import_test_config(test_config_selection_name)
            st.write(test_config_selection_data)
            #for i in test_config_selection_data:
               # st.write(x[i])
                #x[i] = st.text_input("this is a test", "what a world")
                #time.sleep(1)
        else:
            test_config_selection_data = import_test_config(test_config_selection_name)
            st.write(test_config_selection_data) /#TODO  now i need to get the list of keys and then should be able to populate the bubbles
            