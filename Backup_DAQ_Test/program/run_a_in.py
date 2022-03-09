from uldaq import (get_daq_device_inventory, DaqDevice, AInScanFlag, ScanStatus,
                   ScanOption, create_float_buffer, InterfaceType, AiInputMode, AInFlag)
from datetime import datetime
import pandas as pd
import time

def calculate_time_left(run_time, sampling_rate):
  
  loops = sampling_rate*run_time
  sleep_time = 1/sampling_rate

  return loops, sleep_time

def run_ain(ai_device, descriptor,input_mode,ranges,daq_device, channel_names, run_time, sampling_rate):
      print('Active DAQ device: ', descriptor.dev_string, ' (', descriptor.unique_id, ')\n', sep='')      
      data = []
      #print(type(channel_names))


         #making the DICT
      data_dict = {}
      data_dict["DateTime"] = []
      for i in range(len(channel_names)):
        data_dict[channel_names[i]]=[]
      print(type(data_dict))

      loops, sleep_time = calculate_time_left(run_time,sampling_rate)

      for i in range(loops+1):
            now = datetime.now()
            data_dict["DateTime"].append(now)
            for channel in range(len(channel_names)):
                  data = ai_device.a_in(channel, input_mode,ranges[0],AInFlag.DEFAULT)
                  print(data)
                  data_dict[channel_names[channel]].append('{:.6f}'.format(data) )

            time.sleep(sleep_time)
      save_file(data_dict)

def save_file(data_dict ):


        now = datetime.now()
        operator = "Sean Pluemer"
        station_id = "raspberry pi 1"
        pc_name = "raspberry pi"
        dc_configuration = "NA"
        ac_configuration = "NA"
        user_comments = "HELLO WORLD, THIS IS A COMMENT"
        calibration_file = "nan"


        pandas_dataframe_data = pd.DataFrame.from_dict(data_dict, orient='index').transpose()

        template_data = {"operator": operator, "station_id": station_id, "pc_name": pc_name , "dc_configuration": "dc_configuration",
         "ac_configuration": ac_configuration, "user_comments": user_comments, "calibration_file": calibration_file}

        #open text file in read mode
        template_path = "/home/pi/DAQ_Tests/templates/output_template/output_template.dat"
        save_path = "/home/pi/DAQ_Tests/test_data/test_results.csv"

        with open(template_path, 'r') as f:
            template = f.read()

        f = open(save_path, "w")
        f.write(template.format(**template_data))
        f.close()
        pandas_dataframe_data.to_csv(save_path,mode='a', index=False,)

if __name__ == '__main__':
    print("Run_a_in.py was run directly for some reason?")