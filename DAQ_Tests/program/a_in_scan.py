#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Wrapper call demonstrated:        ai_device.a_in_scan()

Purpose:                          Performs a continuous scan of the range
                                  of A/D input channels

Demonstration:                    Displays the analog input data for the
                                  range of user-specified channels using
                                  the first supported range and input mode





Steps:
1.  Call get_daq_device_inventory() to get the list of available DAQ devices
2.  Create a DaqDevice object
3.  Call daq_device.get_ai_device() to get the ai_device object for the AI
    subsystem
4.  Verify the ai_device object is valid
5.  Call ai_device.get_info() to get the ai_info object for the AI subsystem
6.  Verify the analog input subsystem has a hardware pacer
7.  Call daq_device.connect() to establish a UL connection to the DAQ device
8.  Call ai_device.a_in_scan() to start the scan of A/D input channels
9.  Call ai_device.get_scan_status() to check the status of the background
    operation
10. Display the data for each channel
11. Call ai_device.scan_stop() to stop the background operation
12. Call daq_device.disconnect() and daq_device.release() before exiting the
    process.
"""
from __future__ import print_function
from time import sleep
from os import system
from sys import stdout
from datetime import datetime
import pandas as pd
import time

from uldaq import (get_daq_device_inventory, DaqDevice, AInScanFlag, ScanStatus,
                   ScanOption, create_float_buffer, InterfaceType, AiInputMode)


def main():
    """Analog input scan example."""
    daq_device = None
    ai_device = None
    status = ScanStatus.IDLE

    range_index = 0
    interface_type = InterfaceType.ANY
    scan_options = ScanOption.CONTINUOUS
    flags = AInScanFlag.DEFAULT

    file_title = "hello world"
    low_channel, high_channel, samples_per_channel, rate, channel_names = inital_user_input()
    print(len(channel_names))

    #making the DICT
    data_dict = {}
    data_dict["DateTime"] = []
    for i in range(len(channel_names)):
        data_dict[channel_names[i]]=[]

    print(data_dict)    

    try:
        # Get descriptors for all of the available DAQ devices.
        devices = get_daq_device_inventory(interface_type)
        number_of_devices = len(devices)
        if number_of_devices == 0:
            raise RuntimeError('Error: No DAQ devices found')

        print('Found', number_of_devices, 'DAQ device(s):')
        for i in range(number_of_devices):
            print('  [', i, '] ', devices[i].product_name, ' (',
                  devices[i].unique_id, ')', sep='')

        descriptor_index = input('\nPlease select a DAQ device, enter a number'
                                 + ' between 0 and '
                                 + str(number_of_devices - 1) + ': ')
        descriptor_index = int(descriptor_index)
        if descriptor_index not in range(number_of_devices):
            raise RuntimeError('Error: Invalid descriptor index')

        # Create the DAQ device from the descriptor at the specified index.
        daq_device = DaqDevice(devices[descriptor_index])

        # Get the AiDevice object and verify that it is valid.
        ai_device = daq_device.get_ai_device()
        if ai_device is None:
            raise RuntimeError('Error: The DAQ device does not support analog '
                               'input')

        # Verify the specified device supports hardware pacing for analog input.
        ai_info = ai_device.get_info()
        if not ai_info.has_pacer():
            raise RuntimeError('\nError: The specified DAQ device does not '
                               'support hardware paced analog input')

        # Establish a connection to the DAQ device.
        descriptor = daq_device.get_descriptor()
        print('\nConnecting to', descriptor.dev_string, '- please wait...')
        # For Ethernet devices using a connection_code other than the default
        # value of zero, change the line below to enter the desired code.
        daq_device.connect(connection_code=0)

        # The default input mode is SINGLE_ENDED.
        input_mode = AiInputMode.SINGLE_ENDED
        # If SINGLE_ENDED input mode is not supported, set to DIFFERENTIAL.
        if ai_info.get_num_chans_by_mode(AiInputMode.SINGLE_ENDED) <= 0:
            input_mode = AiInputMode.DIFFERENTIAL

        # Get the number of channels and validate the high channel number.
        number_of_channels = ai_info.get_num_chans_by_mode(input_mode)
        if high_channel >= number_of_channels:
            high_channel = number_of_channels - 1
        channel_count = high_channel - low_channel + 1

        # Get a list of supported ranges and validate the range index.
        ranges = ai_info.get_ranges(input_mode)
        if range_index >= len(ranges):
            range_index = len(ranges) - 1

        # Allocate a buffer to receive the data.
        data = create_float_buffer(channel_count, samples_per_channel)

        print('\n', descriptor.dev_string, ' ready', sep='')
        print('    Function demonstrated: ai_device.a_in_scan()')
        print('    Channels: ', low_channel, '-', high_channel)
        print('    Input mode: ', input_mode.name)
        print('    Range: ', ranges[range_index].name)
        print('    Samples per channel: ', samples_per_channel)
        print('    Rate: ', rate, 'Hz')
        print('    Scan options:', display_scan_options(scan_options))
        try:
            input('\nHit ENTER to continue\n')
        except (NameError, SyntaxError):
            pass

        system('clear')

        # Start the acquisition.
        rate = ai_device.a_in_scan(low_channel, high_channel, input_mode,
                                   ranges[range_index], samples_per_channel,
                                   rate, scan_options, flags, data)

        long_term_data = []
        long_term_time = []
        try:
            while True:
            #for lmnop in range(10):
                #print("\n LNNASDJKOFHNASDFASLDKJFHALKJSDF" , lmnop)
                try:
                    # Get the status of the background operation
                    status, transfer_status = ai_device.get_scan_status()

                    #reset_cursor()
                    print('Please enter CTRL + C to terminate the process\n')
                    print('Active DAQ device: ', descriptor.dev_string, ' (',
                          descriptor.unique_id, ')\n', sep='')

                    print('actual scan rate = ', '{:.6f}'.format(rate), 'Hz\n')

                    index = transfer_status.current_index
                    print('currentTotalCount = ',
                          transfer_status.current_total_count)
                    print('currentScanCount = ',
                          transfer_status.current_scan_count)
                    print('currentIndex = ', index, '\n')

                    # Display the data.
                    
                    data_dict["DateTime"].append(datetime.now())
                    for i in range(channel_count):
                        #clear_eol()
                        print(i , channel_count, index)
                        print('chan =',
                              i + low_channel, ': ',
                              '{:.6f}'.format(data[index + i]))
                        data_dict[channel_names[i]].append('{:.6f}'.format(data[index + i]))
                      

                    
                    #print(test)
                        
                    
                   
                   #pandas_dataframe_data = pd.DataFrame.from_dict(data_dict, orient='index').transpose()
                    #print(pandas_dataframe_data)

                   
                    
                     

                    sleep(0.1)
                except (ValueError, NameError, SyntaxError) as e:
                    print(e)
                    print("hello world")
                    
                    break
        except KeyboardInterrupt:
            print("you pressed ctrlc")
            save_file(data_dict)
            pass


    except RuntimeError as error:
        print('\n', error)
        

    finally:
        if daq_device:
            # Stop the acquisition if it is still running.
            

            if status == ScanStatus.RUNNING:
                ai_device.scan_stop()
            if daq_device.is_connected():
                daq_device.disconnect()
            daq_device.release()


def display_scan_options(bit_mask):
    """Create a displays string for all scan options."""
    options = []
    if bit_mask == ScanOption.DEFAULTIO:
        options.append(ScanOption.DEFAULTIO.name)
    for option in ScanOption:
        if option & bit_mask:
            options.append(option.name)
    return ', '.join(options)


def reset_cursor():
    """Reset the cursor in the terminal window."""
    stdout.write('\033[1;1H')


def clear_eol():
    """Clear all characters to the end of the line."""
    stdout.write('\x1b[2K')

def save_file(data_dict ):

    reply = str(raw_input("Would you like to save the file?"+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        file_name = str(raw_input("Please input save file name: ")).lower().strip()
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        operator = "Sean Pluemer"
        station_id = "raspberry pi 1"
        pc_name = "raspberry pi"
        dc_configuration = "NA"
        ac_configuration = "NA"
        user_comments = "HELLO WORLD, THIS IS A COMMENT"
        calibration_file = "nan"
        #pandas_dataframe_data = pd.DataFrame([data_dict])
        pandas_dataframe_data = pd.DataFrame.from_dict(data_dict, orient='index').transpose()
        template_data = {"operator": operator, "station_id": station_id, "pc_name": pc_name , "dc_configuration": "dc_configuration", "ac_configuration": ac_configuration, 
            "user_comments": user_comments, "calibration_file": calibration_file, "long_term_data": pandas_dataframe_data }
        #template_data = {"operator": file_title, "date": dt_string, "sample_rate": sample_rate , "channels_used": str(low_channel) + " - " + str(high_channel), "samples_per_channel": samples_per_channel }
        #open text file in read mode
        path = "/home/pi/Templates/Detl_work/output_template/output_template.dat"
        with open(path, 'r') as f:
            template = f.read()
        #text_file =  open("1st_template.txt", "r")
        #read whole file to a stringc
        #template = text_file.read()
        
        #close file
        #text_file.close()

       # print (template.format(**template_data))

        f = open(file_name, "w")
        f.write(template.format(**template_data))
        f.close()
    if reply[0] == 'n':
        return False

def inital_user_input():
    while True:
        try:
            low_channel = int(input("Please enter the low channel: "))
            
            high_channel = int(input("Please enter the high channel: "))
            if(high_channel < low_channel):
                print("that was not a correct input, please make sure that low < high")
                continue
            samples_per_channel = int(input("How many samples per channel will be used: ")) 
            rate  = int(input("Sampeling Rate: ")) 
            physical_units = None
            total_channels= (high_channel-low_channel+1)
            channel_name = {}
            for i in range(total_channels):
                channel_name[i] = raw_input("Channel %d signal name: " % i)
            #    print(channel_name)
                #while physical_units not in {"volt", "amp"}:
                #    physical_units = raw_input("What is the physical unit (volt or amp): ")
            
            
            
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if (low_channel < 0):
            print("Sorry, your response must not be negative.")
            continue
        else:
            #age was successfully parsed, and we're happy with its value.
            #we're ready to exit the loop.
            break
    return low_channel, high_channel, samples_per_channel, rate, channel_name





if __name__ == '__main__':
    main()
