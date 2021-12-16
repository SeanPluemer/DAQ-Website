import os

import pandas as pd
import streamlit as st


def import_signal_config(csv_file_name, path):
    homepath = "/Users/seanpluemer/Documents/GitHub/DAQ-Website"
    os.chdir(homepath)

    os.chdir(path)

    df = pd.read_csv(csv_file_name)
    os.chdir("/Users/seanpluemer/Documents/GitHub/DAQ-Website")
    return df

path = "src/signal_configs"
df = import_signal_config("SignalConfigTemplate.csv",path)
names = ["Eve", "Alice", "Bob","Eve", "Alice", "Bob","Eve", "Alice", "Bob","Eve", "Alice", "Bob","Eve", "Alice", "Bob","Eve"]
for rows in df:
    st.write(rows)

df.loc[len(names)] = names
st.write(df)
names1 = ["Eveeee", "Alice", "Bob","Eve", "Alice", "Bob","Eve", "Alice", "Bob","Eve", "Alice", "Bob","Eve", "Alice", "Bob","Eve"]
df.loc[0] = names1
st.write(df)
#df = pd.DataFrame("column1", "col 2", "col3")



