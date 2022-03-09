from asyncio import current_task
from curses import start_color
from fcntl import I_CANPUT
from turtle import st
from uldaq import (get_daq_device_inventory, DaqDevice, AInScanFlag, ScanStatus,
                   ScanOption, create_float_buffer, InterfaceType, AiInputMode)

from datetime import datetime
from datetime import timedelta

import pandas as pd
import time
import sys
import csv
from sys import stdout
import os



def run_ain_scan(ai_device, descriptor,input_mode,ranges,daq_device, signal_csv_data, test_csv_data):
      print('Active DAQ device: ', descriptor.dev_string, ' (', descriptor.unique_id, ')\n', sep='')      
      print("here")
      samples_per_channel =    test_csv_data.SamplingRate.max()*2 #Samples per channel is the size of buffer alloted per channel
      scan_options = ScanOption.BLOCKIO
      flags = AInScanFlag.DEFAULT
      

      channel_names = signal_csv_data.Signal_Name.tolist() #get list of the channels
      
      run_time = test_csv_data.TestTime.item() #get the total time that the code needs to run 
      range_index = 0 # sets daq to look for 10v



      ai_info = ai_device.get_info()
      ranges = ai_info.get_ranges(input_mode) #gets voltage ranges from DAQ, inputmode should be single_ended

      channel_count = len(signal_csv_data.Channel) #count number of channels
      data = create_float_buffer(channel_count, samples_per_channel) #makes a circular buffer, this is where the actual data is stored. 

      #rate is the real measured hz
      rate = ai_device.a_in_scan(signal_csv_data.Channel.min(), signal_csv_data.Channel.max(), input_mode,
                                    ranges[range_index], samples_per_channel,
                                    test_csv_data.SamplingRate.max(), scan_options, flags, data) #
      #a_in_scan starts the actual measuring
      print(len(data), channel_count)
      status, transfer_status = ai_device.get_scan_status()
      while (status == ScanStatus.RUNNING): #run code until the time is up
            status, transfer_status = ai_device.get_scan_status()
            os.system('cls||clear')
            print('currentTotalCount = ', transfer_status.current_total_count)
            print('currentScanCount = ', transfer_status.current_scan_count)
            print('currentIndex = ', transfer_status.current_index, '\n')
            time.sleep(0.5)
            for i in range(2):
                        clear_eol()
                        print('chan =', i + signal_csv_data.Channel.min(), ': ', '{:.6f}'.format(data[transfer_status.current_index + i]))


      ai_device.scan_stop()

      save_file(data)

def save_file(data ):
      print(type(data))

      operator = "Sean Pluemer"
      station_id = "raspberry pi 1"
      pc_name = "raspberry pi"
      dc_configuration = "NA"
      ac_configuration = "NA"
      user_comments = "HELLO WORLD, THIS IS A COMMENT"
      calibration_file = "nan"

      template_data = {"operator": operator, "station_id": station_id, "pc_name": pc_name , "dc_configuration": "dc_configuration",
                        "ac_configuration": ac_configuration, "user_comments": user_comments, "calibration_file": calibration_file}

      #open text file in read mode
      template_path = "/home/pi/GitHub/DAQ-Website/DAQ_Tests/templates/output_template/output_template.dat"
      save_path = "/home/pi/GitHub/DAQ-Website/DAQ_Tests/test_data/test_results.csv"
      try:
            with open(template_path, 'r') as f:
                  template = f.read()
                  f = open(save_path, "w")
                  f.write(template.format(**template_data))
                  f.close()
      
            with open(save_path, 'a', newline='') as csvfile: #todo, figure how to seperate the 2 channels 
                  writer = csv.writer(csvfile)
                  for i in range(0, len(data), 2):
                        print(data[i])
                        test = []
                        test.append(data[i])
                        test.append(data[i+1])
                        writer.writerow(test)



      except Exception  as e:
            
            print("something failed in saaving", e)

      print("Save Completed")

def reset_cursor():
    """Reset the cursor in the terminal window."""
    stdout.write('\033[1;1H')

def clear_eol():
    """Clear all characters to the end of the line."""
    stdout.write('\x1b[2K')

if __name__ == '__main__':
    print("Run_a_in.py was run directly for some reason?")