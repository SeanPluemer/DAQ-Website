import time
from datetime import datetime
#import datetime

import streamlit as st
import src.test_configs
import csv_manipulation
import os
import csv
import pandas as pd
import glob

os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
#print(os.getcwd())
def import_test_config(csv_file_name):

    homepath = "/Users/seanpluemer/Documents/GitHub/DAQ-Website"
    os.chdir(homepath)
    path = "src/test_configs"
    os.chdir(path)
    #st.write(csv_file_name)
    if csv_file_name == "New Config":
        csv_file_name = "BlankTestConfigTemplate.csv"
    dict_from_csv = pd.read_csv(csv_file_name, header=None, index_col=0, squeeze=True).to_dict()

    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_of_column_names = []
        for row in csv_reader:
            list_of_column_names.append(row)
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    return dict_from_csv

def app():
    #print(os.getcwd())
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    with st.spinner("Loading  ..."):

        st.write("I should be here")

        # Title the app
        st.title('DAQ Import Config')
        ###################Start Test config settings#######################

        st.markdown("""
         * This is where you will configure new tests 
        """)
        st.subheader('1. Test config setup 🏋️')
        st.write("Import the configuration das file.")
        list_of_test_configs = []
        for list in glob.glob("src/test_configs/*.csv"): #todo might need some logic in herre to get rid of "blank" template
            list_of_test_configs.append(list[17:])

        test_config_selection_name = st.selectbox("Select the test config file", ("New Config" , *list_of_test_configs))
        test_config_selection_data = import_test_config(test_config_selection_name)
        #TODO I was unable to make this work dynamically, so right now i am just doing it manually
        show_test_config_checkbox = st.checkbox('Click to view parameters')
        test_config_values = []
        for values in test_config_selection_data.values():
            test_config_values.append(values)
        if show_test_config_checkbox or test_config_selection_name == "New Config": #todo make new config get rid of checkbox
            st.write(len(test_config_values))


            now = datetime.now().time()  # time object
            current_time = now.strftime("%H:%M")
            st.write(type(now))
#todo, might be worth making this a dictionary
            SamplingRate_text_input = st.text_input("Sampling Rate", test_config_values[0])
            NumOfAvg_text_input = st.text_input("Number of Average", test_config_values[1])
            UpdateRate_text_input = st.text_input("Update Rate", test_config_values[2])
            RecRate_text_input = st.text_input("Rec Rate", test_config_values[3])
            RecRateUnits_text_input = st.selectbox("Rec Rate Units", ("Seconds/Update", "other") )# change
            RecMode_text_input = st.selectbox("Rec Mode", ("Continuous", "other")) #change
            StartTime_text_input = st.time_input('Start Time', now)
            StopTime_text_input = st.time_input("Stop Time", now )
            StartDate_text_input = st.date_input("Start Date", datetime.today())
            StopDate_text_input = st.date_input("Stop Date", datetime.today())
            FileSignals_text_input = st.text_input("File Signals", test_config_values[10]) #todo, not sure for this one...
            FileStats_text_input = st.text_input("File Stats", test_config_values[11])
            AllStats_text_input = st.text_input("All Stats", test_config_values[12])


###################End  Test config settings#######################

###################Start Signal config settings#######################

        st.subheader('2. Signal config setup 🏋️')
        st.write("Import the configuration das file.")
        list_of_signal_configs = []
        for list in glob.glob("src/signal_configs/*.csv"): #todo might need some logic in herre to get rid of "blank" template
            list_of_signal_configs.append(list[17:])

        signal_config_selection_name = st.selectbox("Select the test config file", ("New Config" , *list_of_signal_configs))
        signal_config_selection_name = import_test_config(test_config_selection_name)
        #TODO I was unable to make this work dynamically, so right now i am just doing it manually
        show_signal_config_checkbox = st.checkbox('Click to view singal parameters')
        signal_config_values = []
        
        for values in signal_config_selection_name.values():
            signal_config_values.append(values)
        if show_signal_config_checkbox or signal_config_selection_name == "New Config": #todo make new config get rid of checkbox
            st.write(len(signal_config_values))