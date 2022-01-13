import glob
import os

import numpy as np
import pandas as pd
import streamlit as st

def app():
    with st.spinner("Loading  ..."):
        data_location_path = "src/test_data_from_pi"

        st.write("this is where you can view and download previous test's data. ")
        list_of_test_data = []
        for list in glob.glob(data_location_path+"/*.csv"):  # todo might need some logic in herre to get rid of "blank" template
            list_of_test_data.append(list[22:]) #the 22: crops out the src/test_data_from_pi/
            print(list)
        test_data_selection_name = st.selectbox("Select the test config file", ("test_results.csv", *list_of_test_data))
        if test_data_selection_name != "Click Here":
            test_data_dataframe = import_data(test_data_selection_name, data_location_path)
            print(test_data_dataframe.dtypes)

            #test_data_dataframe =  test_data_dataframe.set_index("DateTime")
            #show_test_config_checkbox = st.checkbox('Click to view parameters')
            #if show_test_config_checkbox:  # or test_config_selection_name == "New Config":

            st.write(test_data_dataframe)

            import altair as alt
            test = pd.melt(test_data_dataframe, id_vars = ['DateTime'] , value_vars =['Voltage ph1', 'amp phB'],var_name ='Signal', value_name ='Value')
            pd.to_datetime(test.DateTime)
            st.write(test.Value.max())

           #_domain =
            st.write(test.head())
            # The basic line
            chart = alt.Chart(test).mark_line().encode(
                x=alt.X('DateTime:T', axis=alt.Axis(format='%H:%M:%S:%L')),
                y=alt.Y('Value:Q', scale=alt.Scale(domain=[test.Value.min(), test.Value.max()])),
                color='Signal:N'
            ).interactive(bind_y = False)



            st.altair_chart(chart, use_container_width=True)


            #st.altair_chart(upper)


def import_data(csv_file_name, path):

    try:

        os.chdir(path)
        parse_dates = ['DateTime']
        df = pd.read_csv(csv_file_name, skiprows=11, index_col=False, parse_dates = parse_dates)
        os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
        return df

    except Exception as e:
        os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
        st.write(e)