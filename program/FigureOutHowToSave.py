'''
This is an example of the a_in. the issue with this, is it samples at whatever rate call the function, not consistnat
from uldaq import(InterfaceType,get_daq_device_inventory,DaqDevice,AiInputMode,AInFlag)

interface_type = InterfaceType.ANY
devices = get_daq_device_inventory(interface_type) #find devices
daq_device = DaqDevice(devices[0]) #make class of the device
daq_device.connect() #connect to device
ai_device = daq_device.get_ai_device()
input_mode = AiInputMode.SINGLE_ENDED
ranges = ai_info.get_ranges(input_mode)
ai_info = ai_device.get_info()


test = ai_device.a_in(0,2,ranges[0],AInFlag.DEFAULT)
print(test)
'''

from uldaq import(InterfaceType, get_daq_device_inventory, DaqDevice, AInScanFlag ,AiInputMode,create_float_buffer,ScanOption,ScanStatus)
import time
import pdb
import sys 
from sys import stdout

def main():

    interface_type = InterfaceType.ANY 
    devices = get_daq_device_inventory(interface_type) #find devices
    daq_device = DaqDevice(devices[0]) #make class of the device
    ai_device = daq_device.get_ai_device() 
    input_mode = AiInputMode.SINGLE_ENDED 
    daq_device.connect(connection_code=0)
    ai_info = ai_device.get_info()
    ranges = ai_info.get_ranges(input_mode)
    descriptor = daq_device.get_descriptor()
    flags = AInScanFlag.DEFAULT

    try:
        low_channel = 0
        high_channel = 1
        samples_per_channel = 100
        rate = 1
        scan_options = ScanOption.CONTINUOUS
        channel_count = high_channel-low_channel +1

        data = create_float_buffer( channel_count, samples_per_channel)
        rate = ai_device.a_in_scan(low_channel,high_channel,input_mode, ranges[0], samples_per_channel, rate, scan_options, flags, data)
        
        try:
            while True:
                try:
                    # Get the status of the background operation
                    status, transfer_status = ai_device.get_scan_status()
                    reset_cursor()
                    print('Please enter CTRL + C to terminate the process\n')
                    print('Active DAQ device: ', descriptor.dev_string, ' (', descriptor.unique_id, ')\n', sep='')

                    print('actual scan rate = ', '{:.6f}'.format(rate), 'Hz\n')

                    index = transfer_status.current_index
                    print('currentTotalCount = ', transfer_status.current_total_count)
                    print('currentScanCount = ', transfer_status.current_scan_count)
                    print('currentIndex = ', index, '\n')

                    # Display the data.
                    for i in range(2):
                        clear_eol()
                        print('chan =', i + low_channel, ': ', '{:.6f}'.format(data[index + i]))
                        time.sleep(0.01)
                    ai_device.scan_wait(WAIT_UNTIL_DONE= 1,)
                except (ValueError, NameError, SyntaxError):
                            break
        except KeyboardInterrupt:
            print("Ctrl c was hit")
            for i in data:
                print(i)
   

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

def reset_cursor():
    """Reset the cursor in the terminal window."""
    stdout.write('\033[1;1H')

def clear_eol():
    """Clear all characters to the end of the line."""
    stdout.write('\x1b[2K')


if __name__ == '__main__':
    main()
