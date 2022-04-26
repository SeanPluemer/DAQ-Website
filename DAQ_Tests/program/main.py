#the goal of this code is to be the central location for all of the DETL DAQ software
import os
from typing_extensions import runtime
import connect_to_daq, run_a_in, run_a_in_scan
import pandas as pd
import sys
import time
import main_waveform
#first step is to read the test parameters and signal configs

def read_test_params():
    signal_csv_data = pd.read_csv("/home/pi/GitHub/DAQ-Website/DAQ_Tests/files_from_server/signal_config.csv",index_col=False)    #print(df)
    test_csv_data = pd.read_csv("/home/pi/GitHub/DAQ-Website/DAQ_Tests/files_from_server/test_config.csv",index_col=False) 
    return signal_csv_data, test_csv_data
#


def main():
    #first step is to read in test parameters, and signal. 
    signal_csv_data, test_csv_data = read_test_params()
    if not (len(signal_csv_data) % 2 ==0):
        sys.exit("signal data needs to be an even input")

    print(test_csv_data)
    
    daq_device = None 
    ai_device, descriptor, input_mode,ranges,daq_device = connect_to_daq.connect(0) #todo, need to find which daq device from server

    run_a_in_scan.run_ain_scan_continuous(ai_device,descriptor,input_mode,ranges,daq_device, signal_csv_data, test_csv_data) 
    #main_waveform.main()

if __name__ == "__main__":
    main()
