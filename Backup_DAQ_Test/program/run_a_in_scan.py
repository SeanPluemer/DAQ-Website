from curses import start_color
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
      data = []
      samples_per_channel =   test_csv_data.SamplingRate.max() #Samples per channel is the size of buffer alloted per channel
      scan_options = ScanOption.CONTINUOUS
      flags = AInScanFlag.DEFAULT

      channel_names = signal_csv_data.Signal_Name.tolist()
      
      run_time = test_csv_data.TestTime.item()
      range_index = 0


      ai_info = ai_device.get_info()
      ranges = ai_info.get_ranges(input_mode)
      if range_index >= len(ranges):
            range_index = len(ranges) - 1

      channel_count = len(signal_csv_data.Channel)
      data = create_float_buffer(channel_count, samples_per_channel)
      rate = ai_device.a_in_scan(signal_csv_data.Channel.min(), signal_csv_data.Channel.max(), input_mode,
                                    ranges[range_index], samples_per_channel,
                                    test_csv_data.SamplingRate.max(), scan_options, flags, data)


      
      #making the DICT
      data_dict = {}
      data_dict["DateTime"] = []
      for i in range(len(channel_names)):
            data_dict[channel_names[i]]=[]

      time_start = time.time()


      while time.time() < time_start + run_time:

            status, transfer_status = ai_device.get_scan_status()
            index = transfer_status.current_index


            data_dict["DateTime"].append(datetime.now())
            for i in range(channel_count):
                        test_data = '{:.6f}'.format(data[index + i])
                        data_dict[channel_names[i]].append('{:.6f}'.format(data[index + i]))


      print("while loop has eneded")
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
      template_path = "/home/pi/DAQ-Website/DAQ_Tests/templates/output_template/output_template.dat"
      save_path = "/home/pi/DAQ-Website/DAQ_Tests/test_data/test_results.csv"
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