import streamlit
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import matplotlib.pyplot as plt

import requests, os
#from gwpy.timeseries import TimeSeries
from gwosc.locate import get_urls
from gwosc import datasets
from gwosc.api import fetch_event_json
import matplotlib as mpl

mpl.use("agg")

from matplotlib.backends.backend_agg import RendererAgg

_lock = RendererAgg.lock

# -- Set page config
apptitle = 'GW Quickview'


st.set_page_config(page_title ="DAQ Demo",
                    initial_sidebar_state="collapsed",
                    page_icon="🔮")
tabs = ["Import Config", "View Data", "Generate Config",  "About"]
page = st.sidebar.radio("Tabs",tabs)



@st.cache(persist=False,
          allow_output_mutation=True,
          suppress_st_warning=False,
          show_spinner= True)

def load_csv():
    df_input = pd.DataFrame()
    df_input = pd.read_csv(input, sep=None, engine='python', encoding='utf-8',
                           parse_dates=True,
                           infer_datetime_format=True)
    return df_input

def prep_data(df):

    df_input = df.rename({metric_col:"y", time_col:"time"},errors='raise',axis=1)
   # df_input = df.rename({date_col: "ds", metric_col: "y"}, errors='raise', axis=1)
    st.markdown("The selected date column is now labeled as **date** and the values columns as **y**")
    df_input = df_input[['time', 'y']]
    df_input =  df_input.sort_values(by='time',ascending=True)
    return df_input

if page == "View Data":
    st.title('DAQ View Data Demo')

    st.markdown("""
         * Use the menu at left to select data and 
         * Your data will appear below
        """)
    st.subheader('1. Data loading 🏋️')
    st.write("Import the output das file.")

    input = st.file_uploader('')
    if input is None:
        st.write("Or use sample dataset to try the application")
        sample = st.checkbox("Download sample from HERE")  # todo change this

    try:
        if sample:
            st.markdown("""[download_link](https://gist.github.com/giandata/e0b5c2d2e71d4fd4388295eb5b71aeeb)""")


    except:

        if input:
            with st.spinner('Loading data..'):
                df = load_csv()

                st.write("Columns:")
                st.write(list(df.columns))
                columns = list(df.columns)

                col2, col3 = st.columns(2)
                #with col1:
                   # date_col = st.selectbox("Select date column", index=0, options=columns, key="date")
                with col2:
                    metric_col = st.selectbox("Select values column", index=0, options=columns, key="values")
                with col3:
                    time_col = st.selectbox("Select time column", index=1, options=columns, key="time")

                df = prep_data(df)
                output = 0

        if st.checkbox('Chart data', key='show'):
            with st.spinner('Plotting data..'):
                col2, col3 = st.columns(2)

                with col3:
                    st.dataframe(df)

                with col2:
                    st.write("Dataframe description:")
                    st.write(df.describe())

            try:
                line_chart = alt.Chart(df).mark_line(point=True).encode(
                    x='time:T',
                    y="y" ).interactive()
                st.altair_chart(line_chart, use_container_width=True)

                st.text(df)


            except:
                st.line_chart(df['y'], use_container_width=True, height=300)


if page == "Import Config":

    # Title the app
    st.title('DAQ Import Config')

    st.markdown("""
     * Use the menu at left to select data and 
     * Your data will appear below
    """)
    st.subheader('1. Data loading 🏋️')
    st.write("Import the configuration das file.")
    with st.expander("Data format"):
        st.write("Click here if you need to generate a config file")
        st.write("Signal Name	Used?	Physical Units	Source	Type	% Error	Last-Modification Date	Range [Max]	Range [Min]	Fwd EU Expression	Rvr EU Expression	Uncertainty Expression	Fwd EU Calibration Points	Rvr EU Calibration Points")

    input = st.file_uploader('')
    if input is None:
        st.write("Or use sample dataset to try the application")
        sample = st.checkbox("Download sample from HERE") #todo change this

    try:
        if sample:
            st.markdown("""[download_link](https://gist.github.com/giandata/e0b5c2d2e71d4fd4388295eb5b71aeeb)""")


    except:

        if input:
            with st.spinner('Loading data..'):
                df = load_csv()

                st.write("Columns:")
                st.write(list(df.columns))
                columns = list(df.columns)

                df = prep_data(df)
                output = 0



    st.sidebar.markdown("## Input Data here:")



if page == "Generate Config":
    # -- Set time by GPS or event
    signal_name_event = st.sidebar.text_input('Signal Name')
    physical_units_event = st.sidebar.selectbox('Units',
                                        ['Volts', 'Amps'])
    source_event = st.sidebar.selectbox('Source of the data?',
                                        ['Dev1/ai0', 'Calculated'])
    data_type_event = st.sidebar.selectbox("Type of data",
                                      ["DC_Voltage", "AC_Voltage", "AC+DC_Voltage", "DC_Amperage", "AC_Amperage", "AC+DC_Amperage",
                                       "Complex_Voltage" , "Complex_Amperage"])

    max_range_event = st.sidebar.text_input('Max Range')
    min_range_event = st.sidebar.text_input('Min Range')
    fwd_eu_expression_event = st.sidebar.text_input('Fwd EU Expression ')
    rvr_Eu_expression_event = st.sidebar.text_input('Rwd EU Expression')
    uncertainty_expression_event = st.sidebar.text_input('Uncertainty Expression')
    fwd_eu_calibration_event = st.sidebar.text_input('Fwd EU Calibration')
    rvr_eu_calibration_event = st.sidebar.text_input('Rwd EU Calibration')

    # -- Choose detector as H1, L1, or V1

st.balloons()

if page == "About":
    st.header("About")

    st.write("")
    st.write("Author:")
    st.markdown(""" Sean Pluemer""")


    st.write("Created on 11/01/2021")
    st.write("Last updated: **11/16/2021**")
