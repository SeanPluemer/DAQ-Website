from asyncio import current_task
from curses import start_color
from fcntl import I_CANPUT
from turtle import st
from uldaq import (get_daq_device_inventory, DaqDevice, AInScanFlag, ScanStatus,
                   ScanOption, create_float_buffer, InterfaceType, AiInputMode)

from datetime import datetime
from datetime import timedelta

import calculate_data

import pandas as pd
import numpy as np
import time
import sys
import csv
from sys import stdout
import os
import threading
import glob


class RepeatedTimer(object): #this is a timer for the program to "run every n seconds"
  def __init__(self, interval, function, *args, **kwargs):
    self._timer = None
    self.interval = interval
    self.function = function
    self.args = args
    self.kwargs = kwargs
    self.is_running = False
    self.next_call = time.time()
    self.start()

  def _run(self):
    self.is_running = False
    self.start()
    self.function(*self.args, **self.kwargs)

  def start(self):
    if not self.is_running:
      self.next_call += self.interval
      self._timer = threading.Timer(self.next_call - time.time(), self._run)
      self._timer.start()
      self.is_running = True

  def stop(self):
    self._timer.cancel()
    self.is_running = False

def run_ain_scan_continuous(ai_device, descriptor,input_mode,ranges,daq_device, signal_csv_data, test_csv_data):
      print('Active DAQ device: ', descriptor.dev_string, ' (', descriptor.unique_id, ')\n', sep='')      
      run_time = test_csv_data.TestTime.item() #get the total time that the code needs to run 
      save_time = test_csv_data.RecRate.item()
      whole_waveform_save_time = test_csv_data.UpdateRate.item()
      signal_count = len(signal_csv_data.Signal_Name)
      sample_rate = test_csv_data.SamplingRate.max()

      samples_per_channel =    sample_rate*signal_count #Samples per channel is the size of buffer alloted per channel
      scan_options = ScanOption.CONTINUOUS
      flags = AInScanFlag.DEFAULT

      channel_names = signal_csv_data.Signal_Name.tolist() #get list of the channels      
      range_index = 0 # sets daq to look for 10v
      ai_info = ai_device.get_info()
      ranges = ai_info.get_ranges(input_mode) #gets voltage ranges from DAQ, inputmode should be single_ended

      channel_count = len(signal_csv_data.Channel) #count number of channels
      data = create_float_buffer(channel_count, samples_per_channel) #makes a circular buffer, this is where the actual data is stored. 

      #rate is the real measured hz
      create_initial_csv(channel_names)
      rate = ai_device.a_in_scan(signal_csv_data.Channel.min(), signal_csv_data.Channel.max(), input_mode,
                                    ranges[range_index], samples_per_channel,
                                    test_csv_data.SamplingRate.max(), scan_options, flags, data) #

      #a_in_scan starts the actual measuring
      status, transfer_status = ai_device.get_scan_status()
      for f in glob.glob("/home/pi/GitHub/DAQ-Website/DAQ_Tests/test_data/waveform/*"):
                  os.remove(f)


      time.sleep(3)#this delay is to ensure the daq starts and buffer is filling

      starttime = time.time()
      rt = RepeatedTimer(save_time, perform_calculations, data, signal_csv_data, sample_rate ) 
      whole_waveform = RepeatedTimer(whole_waveform_save_time, save_whole_waveform, data,  signal_csv_data )
      try:
            while (status == ScanStatus.RUNNING): #run code until the time is up
                  try:
                        if stop_trigger():
                              print("Stop Called")
                              perform_calculations(data,signal_csv_data, sample_rate)
                              ai_device.scan_stop()
                              break
                        if(time.time() - starttime > run_time):
                              ai_device.scan_stop()
                              break

                        status, transfer_status = ai_device.get_scan_status()
                        os.system('cls||clear')
                        print("Real Rate = ", rate, "Hz")
                        print('currentTotalCount = ', transfer_status.current_total_count)
                        print('currentScanCount = ', transfer_status.current_scan_count)
                        print('currentIndex = ', transfer_status.current_index, '\n')

                        time.sleep(1)

                  except Exception as e:
                        print("in exception: ", e)
                        ai_device.scan_stop()
                        rt.stop
                        
                        
      finally:
            rt.stop()
            whole_waveform.stop()
            ai_device.scan_stop()
            

def save_whole_waveform(data,signal_csv_data):
      signal_count = len(signal_csv_data.Signal_Name)
      date_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")

      with open('/home/pi/GitHub/DAQ-Website/DAQ_Tests/test_data/waveform/WholeWaveform_' + str(date_time) + '.csv', 'w') as csvfile:
            writer=csv.writer(csvfile, delimiter=',')
            for signal in range(signal_count): #this will put all the signals in diff indexes 
                  seperated_signals = (data[signal::signal_count])
                  writer.writerow([signal_csv_data.Signal_Name[signal], seperated_signals])
            

def stop_trigger():
      return os.path.exists("/home/pi/GitHub/DAQ-Website/DAQ_Tests/files_from_server/stop.txt")


def perform_calculations(data,signal_csv_data, sample_rate): 
      signal_count = len(signal_csv_data.Signal_Name)
      channel_names = signal_csv_data.Signal_Name.tolist() #get list of the channels   

      seperated_signals = [] 
      for signal in range(signal_count): #this will put all the signals in diff indexes 
            seperated_signals.append(data[signal::signal_count])

      t=[] #t is the time between two measurements
      temp = 0
      for i in range(len(seperated_signals[0])):
            t.append(temp)
            temp+=1/sample_rate

      v_rms = calculate_data.calc_RMS(seperated_signals[0]) #calculates RMS 
      a_rms = calculate_data.calc_RMS(seperated_signals[1])
      
      #now to figure out when I am doing calculations

     # with open('everything_else.csv', 'w') as csvfile:
      #      writer=csv.writer(csvfile, delimiter=',')
       #     writer.writerows(zip(t, seperated_signals[0],seperated_signals[1]))

      #everything_else = calculate_data.pf_from_waveform(np.array(t)[:1000],np.array(seperated_signals[0][:1000]),np.array(seperated_signals[1][:1000]), sample_rate) 
      #todo, this is not working at the moment^ fix 

      frequency = 60
      avg_P, P1, PH, N, Q1, DI, DV, S, S1, SN, SH, PF1, PF, har_poll,  THD_V, THD_I = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

      S,PF,avg_P = calculate_data.temp_calc(v_rms,a_rms,np.array(seperated_signals[0]),np.array(seperated_signals[1]))

      date = datetime.now().strftime("%d/%m/%Y")
      date_time = datetime.now().strftime("%H:%M:%S")

      #signal_data = [date, date_time, v_rms, a_rms, frequency, avg_P, P1, PH, N, Q1, DI, DV, S, S1, SN, SH, PF1, PF, har_poll, THD_V, THD_I]
      signal_data = [date, date_time, v_rms, a_rms, frequency, avg_P, S, PF]

      save_n_seconds(signal_data)

def save_n_seconds(data): 
      """ THis function should be responsible for saving the "n seconds" time 
      """
      save_path = "/home/pi/GitHub/DAQ-Website/DAQ_Tests/test_data/test_results.csv"
      try:
            with open(save_path, 'a', newline='') as csvfile: #todo, figure how to seperate the 2 channels 
                  writer = csv.writer(csvfile)
                  writer.writerow(data)
      except Exception  as e:
            print("something failed in saving the n_seconds", e)

      #So i need a way to know what files to save and what files to disregard
      #on top of that, i need a way to figure out what signal this is saving, what if there are multiple voltages and currents? 
      

def create_initial_csv(channel_names):
      operator = "Sean Pluemer"
      station_id = "raspberry pi 1"
      pc_name = "raspberry pi"
      dc_configuration = "NA"
      ac_configuration = "NA"
      user_comments = "HELLO WORLD, THIS IS A COMMENT"
      calibration_file = "nan"

      template_data = {"operator": operator, "station_id": station_id, "pc_name": pc_name , "dc_configuration": "dc_configuration",
                        "ac_configuration": ac_configuration, "user_comments": user_comments, "calibration_file": calibration_file}

      template_path = "/home/pi/GitHub/DAQ-Website/DAQ_Tests/templates/output_template/output_template.dat"
      save_path = "/home/pi/GitHub/DAQ-Website/DAQ_Tests/test_data/test_results.csv"
      channel_names.insert(0, "Date")
      channel_names.insert(1, "Time")

      try:
            with open(template_path, 'r') as f:
                  template = f.read()
                  with open(save_path, 'w') as a:
                        values_writer = csv.writer(a, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        a.write(template.format(**template_data))
                        values_writer.writerow(channel_names)

      except Exception  as e:
            print("something failed in saving the intial file", e)
      print("Initial Save Completed")

def save_file(data ):
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
def run_ain_scan_blockIO(ai_device, descriptor,input_mode,ranges,daq_device, signal_csv_data, test_csv_data):
      print('Active DAQ device: ', descriptor.dev_string, ' (', descriptor.unique_id, ')\n', sep='')      
      run_time = test_csv_data.TestTime.item() #get the total time that the code needs to run 

      samples_per_channel =    test_csv_data.SamplingRate.max()*run_time #Samples per channel is the size of buffer alloted per channel
      scan_options = ScanOption.CONTINUOUS
      flags = AInScanFlag.DEFAULT

      channel_names = signal_csv_data.Signal_Name.tolist() #get list of the channels      
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
      status, transfer_status = ai_device.get_scan_status()
      while (status == ScanStatus.RUNNING): #run code until the time is up
            status, transfer_status = ai_device.get_scan_status()
            os.system('cls||clear')
            print("Real Rate = ", rate, "Hz")
            print('currentTotalCount = ', transfer_status.current_total_count)
            print('currentScanCount = ', transfer_status.current_scan_count)
            print('currentIndex = ', transfer_status.current_index, '\n')
            time.sleep(0.5)
            
            
      save_file(data)