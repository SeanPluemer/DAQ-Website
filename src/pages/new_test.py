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
def import_test_config(csv_file_name, path):

    homepath = "/Users/seanpluemer/Documents/GitHub/DAQ-Website"
    os.chdir(homepath)

    os.chdir(path)


    file = open(csv_file_name)


    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)



    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    return header, rows

def app():
    #print(os.getcwd())
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    with st.spinner("Loading  ..."):


        # Title the app
        st.title('DAQ Import Config')
        ###################Start Test config settings#######################
        path = "src/test_configs"
        st.markdown("""
         * This is where you will configure new tests 
        """)
        st.subheader('1. Test config setup 🏋️')
        st.write("Import the configuration das file.")
        list_of_test_configs = []
        for list in glob.glob("src/test_configs/*.csv"): #todo might need some logic in herre to get rid of "blank" template
            list_of_test_configs.append(list[17:])

        test_config_selection_name = st.selectbox("Select the test config file", ("New Config" , *list_of_test_configs))
        if test_config_selection_name == "New Config":
            test_config_selection_name = "BlankTestConfigTemplate.csv"
        test_config_selection_data_keys, test_config_values = import_test_config(test_config_selection_name, path)
        #TODO I was unable to make this work dynamically, so right now i am just doing it manually
        show_test_config_checkbox = st.checkbox('Click to view parameters')
        if show_test_config_checkbox:# or test_config_selection_name == "New Config": #todo make new config get rid of checkbox
            st.write(test_config_values[0][0 ])


            now = datetime.now().time()  # time object
            current_time = now.strftime("%H:%M")
            st.write(type(now))
#todo, might be worth making this a dictionary
            SamplingRate_text_input = st.text_input("Sampling Rate", test_config_values[0][0])
            NumOfAvg_text_input = st.text_input("Number of Average", test_config_values[0][1])
            UpdateRate_text_input = st.text_input("Update Rate", test_config_values[0][2])
            RecRate_text_input = st.text_input("Rec Rate", test_config_values[0][3])
            RecRateUnits_text_input = st.selectbox("Rec Rate Units", ("Seconds/Update", "other") )# change
            RecMode_text_input = st.selectbox("Rec Mode", ("Continuous", "other")) #change
            StartTime_text_input = st.time_input('Start Time', now)
            StopTime_text_input = st.time_input("Stop Time", now )
            StartDate_text_input = st.date_input("Start Date", datetime.today())
            StopDate_text_input = st.date_input("Stop Date", datetime.today())
            FileSignals_text_input = st.text_input("File Signals", test_config_values[0][10]) #todo, not sure for this one...
            FileStats_text_input = st.text_input("File Stats", test_config_values[0][11])
            AllStats_text_input = st.text_input("All Stats", test_config_values[0][12])


###################End  Test config settings#######################

###################Start Signal config settings#######################
        path = "src/signal_configs"
        st.subheader('2. Signal config setup 🏋️')
        st.write("Import the configuration das file.")
        list_of_signal_configs = []
        for list in glob.glob("src/signal_configs/*.csv"): #todo might need some logic in herre to get rid of "blank" template
            list_of_signal_configs.append(list[19:])

        signal_config_selection_name = st.selectbox("Select the test config file", ("New Config" , *list_of_signal_configs))
        if signal_config_selection_name == "New Config":
            signal_config_selection_name = "SignalConfigTemplate.csv"
        signal_config_selection_data_keys, signal_config_selection_data_values = import_test_config(signal_config_selection_name,path)


        #TODO I was unable to make this work dynamically, so right now i am just doing it manually
        show_signal_config_checkbox = st.checkbox('Click to view singal parameters')



        if show_signal_config_checkbox or signal_config_selection_name == "New Config": #todo make new config get rid of checkbox

            st.write(signal_config_selection_data_values)
#todo, now to figure how to write a signal