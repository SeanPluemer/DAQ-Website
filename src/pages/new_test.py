import time
from datetime import datetime
# import datetime
from random import random

import numpy as np
import streamlit as st
import src.test_configs
import csv_manipulation
import os
import csv
import pandas as pd
import glob

os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")

def import_signal_config(csv_file_name, path):
    homepath = "/Users/seanpluemer/Documents/GitHub/DAQ-Website"
    os.chdir(homepath)

    os.chdir(path)

    df = pd.read_csv(csv_file_name)
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    return df

# print(os.getcwd())
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


import random
import string

if 'count' not in st.session_state:  # not sure what this does
    st.session_state.count = 0
testdata = []


def add_new_row():
    testdata = st.text_input("Please input something",
                             key=random.choice(string.ascii_uppercase) + str(random.randint(0, 999999)))
    st.write(testdata)
    return testdata


def app():
    # print(os.getcwd())
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    with st.spinner("Loading  ..."):

        # Title the app
        st.title('DAQ Import Config')
        ###################Start Test config settings#######################
        path = "src/test_configs"
        st.markdown("""* This is where you will configure new tests""")
        st.subheader('1. Test config setup 🏋️')
        st.write("Import the configuration das file.")
        list_of_test_configs = []
        for list in glob.glob("src/test_configs/*.csv"):  # todo might need some logic in herre to get rid of "blank" template
            list_of_test_configs.append(list[17:])
        test_config_selection_name = st.selectbox("Select the test config file", ("New Config", *list_of_test_configs))

        if test_config_selection_name == "New Config":
            test_config_selection_name = "BlankTestConfigTemplate.csv"
        test_config_selection_dataframe= import_signal_config(test_config_selection_name, path)
        # TODO I was unable to make this work dynamically, so right now i am just doing it manually
        show_test_config_checkbox = st.checkbox('Click to view parameters')
        if show_test_config_checkbox:  # or test_config_selection_name == "New Config": #todo make new config get rid of checkbox
            st.write(test_config_selection_dataframe)



        """
            now = datetime.now().time()  # time object
            current_time = now.strftime("%H:%M")
            st.write(type(now))
            # todo, might be worth making this a dictionary
            SamplingRate_text_input = st.text_input("Sampling Rate", test_config_values[0][0])
            NumOfAvg_text_input = st.text_input("Number of Average", test_config_values[0][1])
            UpdateRate_text_input = st.text_input("Update Rate", test_config_values[0][2])
            RecRate_text_input = st.text_input("Rec Rate", test_config_values[0][3])
            RecRateUnits_text_input = st.selectbox("Rec Rate Units", ("Seconds/Update", "other"))  # change
            RecMode_text_input = st.selectbox("Rec Mode", ("Continuous", "other"))  # change
            StartTime_text_input = st.time_input('Start Time', now)
            StopTime_text_input = st.time_input("Stop Time", now)
            StartDate_text_input = st.date_input("Start Date", datetime.today())
            StopDate_text_input = st.date_input("Stop Date", datetime.today())
            FileSignals_text_input = st.text_input("File Signals",
                                                   test_config_values[0][10])  # todo, not sure for this one...
            FileStats_text_input = st.text_input("File Stats", test_config_values[0][11])
            AllStats_text_input = st.text_input("All Stats", test_config_values[0][12])
            text = st.text_input("Type here")

            text2 = st.text_input("Type here", key="last_name")
###################End  Test config settings#######################
        ###################Start Signal config settings#######################
        """
        path = "src/signal_configs"
        st.subheader('2. Signal config setup 🏋️')
        st.write("Import the configuration das file.")
        list_of_signal_configs = []
        for list in glob.glob("src/signal_configs/*.csv"):  # todo might need some logic in herre to get rid of "blank" template
            list_of_signal_configs.append(list[19:])

        signal_config_selection_name = st.selectbox("Select the test config file",
                                                    ("New Config", *list_of_signal_configs))
        if signal_config_selection_name == "New Config":
            signal_config_selection_name = "SignalConfigTemplate.csv"

            test =  make_new_signal(import_signal_config(signal_config_selection_name,path),0)
            st.write(test)


        signal_selection_dataframe =import_signal_config(signal_config_selection_name,path)



        # TODO I was unable to make this work dynamically, so right now i am just doing it manually
        show_signal_config_checkbox = st.checkbox('Click to view singal parameters')

        if show_signal_config_checkbox or signal_config_selection_name == "New Config":  # todo make new config get rid of checkbox
            st.write(signal_selection_dataframe)
            #st.write(signal_selection_dataframe.columns.values.tolist())
            #todo I dont need this right now, but this might be useful in the future



            if st.button("Add new Signal"):
                st.session_state.count += 1
                # r st.write(st.session_state.count)
                hellovar = add_new_row()
                st.write(hellovar)
                if st.session_state.count > 1:
                    for i in range(st.session_state.count - 1):
                        st.write(i)
                        add_new_row()
# todo, now to figure how to write a signal
def make_new_signal(template_data_frame, count):
    st.write(count)
    st.write(template_data_frame)

    new_file_name = st.text_input("What do you want to name this config")


    signal_name = st.text_input("Name of signal")
    template_data_frame = template_data_frame.append({'Signal Name': signal_name}, ignore_index=True)
    a, b, c, d = st.columns(4)
    signal_used = a.selectbox("Will the signal be used?", ("Used", "Not Used"))
    physical_units = b.selectbox('Units',['Volts', 'Amps', "Watts", "VA", "VARs", "Frequency", "Deg C", "N/A"])
    signal_source = c.selectbox("Source", ["TBD", "Calculated"]) #todo this will need to be worked on to find the sources
    signal_type = d.selectbox("Type of data",["DC_Voltage", "AC_Voltage", "AC+DC_Voltage", "DC_Amperage", "AC_Amperage", "AC+DC_Amperage",
                                       "Complex_Voltage" , "Complex_Amperage"])
    d, e, f = st.columns(3)
    signal_error = d.text_input("% Error")
    max_range = e.text_input('Max Range')
    min_range = f.text_input('Min Range')
    fwd_eu_expression = st.text_input('Fwd EU Expression ')
    rvr_Eu_expression = st.text_input('Rwd EU Expression')
    uncertainty_expression= st.text_input('Uncertainty Expression')
    fwd_eu_calibration = st.text_input('Fwd EU Calibration')
    rvr_eu_calibration  = st.text_input('Rwd EU Calibration')
    signal_notes = st.text_input("Notes (not used for test)")
    joined_string = [signal_name, signal_used, physical_units, signal_source, signal_type,
            signal_error,max_range,min_range,fwd_eu_expression,rvr_Eu_expression,uncertainty_expression,
            fwd_eu_calibration,rvr_eu_calibration,signal_notes]
   # for i in range(1):
    template_data_frame.loc[count] = [joined_string]
    st.write(template_data_frame)
    new_signal, finish_signal = st.columns(2)
    if new_signal.button("New Signal"):
        st.write("reuslt is True")
        make_new_signal(template_data_frame, count+1)
    else:
        st.write("reuslt is false")
    finish_signal.button("Finish and Save") #todo i would like to change the color of this button, but dont think its possible.
    return template_data_frame

#Todo, i am stuck on the "add new signal part"


