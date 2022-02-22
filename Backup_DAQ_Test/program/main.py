#the goal of this code is to be the central location for all of the DETL DAQ software
from os import terminal_size
from typing_extensions import runtime
import connect_to_daq, run_a_in, run_a_in_scan
import pandas as pd
#first step is to read the test parameters and signal configs

def read_test_params():
    signal_csv_data = pd.read_csv("/home/pi/DAQ-Website/DAQ_Tests/files_from_server/signal_config.csv",index_col=False)    #print(df)
    test_csv_data = pd.read_csv("/home/pi/DAQ-Website/DAQ_Tests/files_from_server/test_config.csv",index_col=False) 
    return signal_csv_data, test_csv_data
#

#first step is to connect to the DAQ device


#1/5/22 I left off here, I am trying to get the csv to save but am getting a problem having it ... ... ... the data, goes from 4 to 995
#I will then try to store the data from a_in.py 
#i will then filter the data from the selected channel


def main():
    #first step is to read in test parameters, and signal. 
    signal_csv_data, test_csv_data = read_test_params()
    print(test_csv_data)


    daq_device = None 
    ai_device, descriptor, input_mode,ranges,daq_device = connect_to_daq.connect(0) #todo, need to find which daq device from server


    #run_a_in.run_ain(ai_device,descriptor,input_mode,ranges,daq_device, channel_names, run_time, sampling_rate) 


    run_a_in_scan.run_ain_scan(ai_device,descriptor,input_mode,ranges,daq_device, signal_csv_data, test_csv_data) 


if __name__ == "__main__":
    main()
