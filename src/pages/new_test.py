from datetime import datetime
import streamlit as st
import os
import csv
import pandas as pd
import glob
import shutil
from src.programs import connect_to_pi

os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")

def import_signal_config(csv_file_name, path):
    homepath = "/Users/seanpluemer/Documents/GitHub/DAQ-Website"
    os.chdir(homepath)

    os.chdir(path)

    df = pd.read_csv(csv_file_name,index_col=False)
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    print(type(df))
    return df

def import_test_config(csv_file_name, path):
    homepath = "/Users/seanpluemer/Documents/GitHub/DAQ-Website"
    os.chdir(homepath)

    os.chdir(path)

    df = pd.read_csv(csv_file_name)
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    return df


def app():
    # print(os.getcwd())
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    with st.spinner("Loading  ..."):
        # Title the app

        st.title('DAQ Import Config')
        ###################Start Test config settings#######################
        path = "src/test_configs"
        if "hello" not in st.session_state:
            st.session_state["hello"] = 0
            st.session_state["new_signal"]=0

        st.markdown("""* This is where you will configure new tests""")
        st.subheader('1. Test config setup 🏋️')
        st.write("Import the configuration das file.")
        list_of_test_configs = []
        for list in glob.glob("src/test_configs/*.csv"):  # todo might need some logic in herre to get rid of "blank" template
            list_of_test_configs.append(list[17:])
        test_config_selection_name = st.selectbox("Select the test config file", ("New Config", *list_of_test_configs))
        if test_config_selection_name == "New Config":
            show_new_test_config_checkbox = st.checkbox('Click to input new Test ')
            #signal_config_selection_name = "SignalConfigTemplate.csv"
            if show_new_test_config_checkbox:
                make_new_test(import_test_config("BlankTestConfigTemplate.csv",path))# this will make a csv file and save it
                #todo, the only way is to reload the page, to get the new csv to show up
        if test_config_selection_name != "New Config":

            test_config_selection_dataframe= import_signal_config(test_config_selection_name, path)
            # TODO I was unable to make this work dynamically, so right now i am just doing it manually
            show_test_config_checkbox = st.checkbox('Click to view parameters')
            if show_test_config_checkbox:  # or test_config_selection_name == "New Config": #todo make new config get rid of checkbox
                st.write(test_config_selection_dataframe)


###################End  Test config settings#######################
        ###################Start Signal config settings#######################
        path = "src/signal_configs"
        st.subheader('2. Signal config setup 🏋️')
        st.write("Import the configuration das file.")
        list_of_signal_configs = []


        for list in glob.glob("src/signal_configs/*.csv"):  # todo might need some logic in herre to get rid of "blank" template
            list_of_signal_configs.append(list[19:])

        signal_config_selection_name = st.selectbox("Select the test config file",
                                                    ("New Config", *list_of_signal_configs))

        if signal_config_selection_name == "New Config":
            show_new_signal_config_checkbox = st.checkbox('Click to input new Signal ')
            #signal_config_selection_name = "SignalConfigTemplate.csv"
            if show_new_signal_config_checkbox:
                make_new_signal(import_signal_config("SignalConfigTemplate.csv",path))# this will make a csv file and save it
                #todo, the only way is to reload the page, to get the new csv to show up
        if signal_config_selection_name != "New Config":
            signal_selection_dataframe =import_signal_config(signal_config_selection_name,path)

            # TODO I was unable to make this work dynamically, so right now i am just doing it manually
            show_signal_config_checkbox = st.checkbox('Click to view singal parameters')
            if show_signal_config_checkbox or signal_config_selection_name == "New Config":  # todo make new config get rid of checkbox
                print(type(signal_selection_dataframe))
                st.write(signal_selection_dataframe)
                #st.write(signal_selection_dataframe.columns.values.tolist())
                #todo I dont need this right now, but this might be useful in the future


#this is where the data is getting sent to the raspberry pi
        if signal_config_selection_name != "New Config" and test_config_selection_name != "New Config":
            if st.button("Start Test"):
                pi_status = st.write("Connecting to pi")

                pi_path = '/home/pi/DAQ_Tests/files_from_server'
                signal_path =  "/Users/seanpluemer/Documents/GitHub/DAQ-Website/src/signal_configs/" + signal_config_selection_name
                test_path =  "/Users/seanpluemer/Documents/GitHub/DAQ-Website/src/test_configs/" + test_config_selection_name
                connect_to_pi.copy_files_to_pi(signal_path, test_path, pi_path)
                #connect_to_pi.run_cmd("python3  demo.py " + signal_config_selection_name + " " + test_config_selection_name, pi_path )
                del pi_status
                pi_status = st.write("connected") #todo, i was right here (12/21)

        if st.button("pull data"):
            pi_path = '/home/pi/learning_connection/'
            connect_to_pi.copy_files_from_pi("test.txt", pi_path)





# todo, now to figure how to write a signal
def make_new_test(template_data_frame):
    new_file_name = st.text_input("What do you want to name this config")  # todo, make sure this is an okay name
    with st.form("test_form", clear_on_submit=True):

        now = datetime.now().time()  # time object
        current_time = now.strftime("%H:%M")
        a, b, c, d = st.columns(4)
        SamplingRate_text_input = a.text_input("Sampling Rate", )
        NumOfAvg_text_input = b.text_input("Number of Average")
        UpdateRate_text_input = c.text_input("Update Rate")
        RecRate_text_input = d.text_input("Rec Rate")
        e,f = st.columns(2)
        RecRateUnits_text_input = e.selectbox("Rec Rate Units", ("Seconds/Update", "other"))  # change
        RecMode_text_input = f.selectbox("Rec Mode", ("Continuous", "other"))  # change
        g,h,i,j = st.columns(4)

        StartTime_text_input = g.time_input('Start Time', now)
        StopTime_text_input = h.time_input("Stop Time", now)
        StartDate_text_input = i.date_input("Start Date", datetime.today())
        StopDate_text_input = j.date_input("Stop Date", datetime.today())
        FileSignals_text_input = st.text_input("File Signals")  # todo, not sure for this one...
        FileStats_text_input = st.text_input("File Stats")
        AllStats_text_input = st.text_input("All Stats")
        test_notes = st.text_input("Notes (not used for test)")
        st.write(UpdateRate_text_input)
        joined_string = [SamplingRate_text_input, NumOfAvg_text_input, UpdateRate_text_input, RecMode_text_input, RecRate_text_input,
                         RecMode_text_input, StartTime_text_input, StopTime_text_input, StartDate_text_input, StopDate_text_input,
                         FileSignals_text_input,
                         FileStats_text_input, AllStats_text_input, test_notes]
        st.write(joined_string)

        submitted = st.form_submit_button("Finish")

        if submitted: #todo, make checks for data input
            shutil.copy('src/test_configs/BlankTestConfigTemplate.csv', 'src/test_configs/'+new_file_name)
            f = open('src/test_configs/'+new_file_name, 'a+', newline='')
            writer = csv.writer(f)
            writer.writerow(joined_string)
            f.close()
            st.write("Test Config Successfully Saved")


def make_new_signal(template_data_frame):
#    st.write(template_data_frame)

    new_signal_file_name = st.text_input("What do you want to name this config")#todo, make sure this is an okay name
    with st.form("signal_form", clear_on_submit=True):

        signal_name = st.text_input("Name of signal")
        st.write(type(signal_name))
        #template_data_frame.append({'Signal Name': signal_name}, ignore_index=True)
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
        st.write(joined_string)


        submitted = st.form_submit_button("Save Signal")

        if submitted:
            if st.session_state.new_signal ==0:
                shutil.copy('src/signal_configs/SignalConfigTemplate.csv', 'src/signal_configs/tempcsvdata.csv')

            st.session_state.new_signal += 1
            f = open('src/signal_configs/tempcsvdata.csv', 'a+', newline='')
            writer = csv.writer(f)
            writer.writerow(joined_string)
            f.close()

            st.write(import_signal_config("tempcsvdata.csv", "src/signal_configs"))

    if st.button("Finish"):
        os.rename("src/signal_configs/tempcsvdata.csv", "src/signal_configs/"+new_signal_file_name)

    return template_data_frame



