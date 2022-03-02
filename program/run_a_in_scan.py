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


def run_ain_scan(ai_device, descriptor,input_mode,ranges,daq_device, signal_csv_data, test_csv_data):

      print('Active DAQ device: ', descriptor.dev_string, ' (', descriptor.unique_id, ')\n', sep='')      
 
      samples_per_channel =   test_csv_data.SamplingRate.max() #Samples per channel is the size of buffer alloted per channel
      scan_options = ScanOption.CONTINUOUS
      flags = AInScanFlag.DEFAULT

      channel_names = signal_csv_data.Signal_Name.tolist() #get list of the channels
      
      run_time = test_csv_data.TestTime.item() #get the total time that the code needs to run 
      range_index = 0 # sets daq to look for 10v



      ai_info = ai_device.get_info()
      ranges = ai_info.get_ranges(input_mode) #gets voltage ranges from DAQ, inputmode should be single_ended

      channel_count = len(signal_csv_data.Channel) #count number of channels
      data = create_float_buffer(channel_count, samples_per_channel*10) #makes a circular buffer, this is where the actual data is stored. 

      #rate is the real measured hz
      rate = ai_device.a_in_scan(signal_csv_data.Channel.min(), signal_csv_data.Channel.max(), input_mode,
                                    ranges[range_index], samples_per_channel,
                                    test_csv_data.SamplingRate.max(), scan_options, flags, data) 
      #a_in_scan starts the actual measuring


      
      #making the DICT
      data_dict = {}
      data_dict["DateTime"] = []
      for i in range(len(channel_names)):
            data_dict[channel_names[i]]=[]

      time_start = time.time()

      last_scan_number = 0
      total_samples = test_csv_data.SamplingRate.max() * test_csv_data.TestTime.item() #how many inputs the loop has to run, time * sample rate

      status, transfer_status = ai_device.get_scan_status()
      current_scan = transfer_status.current_scan_count #this is how many "samples" per channel there have been
      print(current_scan)

      while (total_samples >= current_scan ): #run code until the time is up
            status, transfer_status = ai_device.get_scan_status()
            index = transfer_status.current_index #index is the location its at in the buffer
            current_scan = transfer_status.current_scan_count
            #print(current_scan)
            #print(transfer_status.current_scan_count)
            #print(rate)
            
            '''if(last_scan_number != current_scan): #this means that, there has been a change in the measurmnet 
            #commenting this out, because I dont think this is the correct logic 
                  print("adding data")
                  last_scan_number = current_scan

                  data_dict["DateTime"].append(datetime.now())
                  for i in range(channel_count):
                              test_data = '{:.6f}'.format(data[index + i])
                              data_dict[channel_names[i]].append('{:.6f}'.format(data[index + i]))
            #Data is being updated always in the background. I need a way to check when its updated save the data.  '''
            # maybe one method is to see if the current scan is = to the last scan, update the data.                  
            data_dict["DateTime"].append(datetime.now())
            for i in range(channel_count):
                  test_data = '{:.6f}'.format(data[index + i])
                  data_dict[channel_names[i]].append('{:.6f}'.format(data[index + i]))


      ai_device.scan_stop()
      for i in data:
            print(i)
      save_file(data_dict)

def save_file(data_dict ):
      print(sys.getsizeof(data_dict))

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
      
            with open(save_path, 'a', newline='') as csvfile:
                  writer = csv.DictWriter(csvfile, data_dict.keys())
                  writer.writeheader()
                  for i in range(len(list(data_dict.values())[0])):
                        writer.writerow({key:data_dict[key][i] for key in data_dict.keys()}) 
      except:
            print("something failed in saaving")

      print("Save Completed")

if __name__ == '__main__':
    print("Run_a_in.py was run directly for some reason?")