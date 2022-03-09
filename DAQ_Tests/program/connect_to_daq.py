from uldaq import (get_daq_device_inventory, DaqDevice, AInScanFlag, ScanStatus,
                   ScanOption, create_float_buffer, InterfaceType, AiInputMode, AInFlag)
interface_type = InterfaceType.ANY
import time

def view_daq_devices():
    devices = get_daq_device_inventory(interface_type)
    number_of_devices = len(devices)
    if number_of_devices == 0:
        raise RuntimeError('Error: No DAQ devices found')

    print('Found', number_of_devices, 'DAQ device(s):')
    for i in range(number_of_devices):
                print('  [', i, '] ', devices[i].product_name, ' (',devices[i].unique_id, ')', sep='')

def connect(descriptor_index):
    try:
            range_index = 0
            devices = get_daq_device_inventory(interface_type)
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
                print("HELLO MY INPUT MODE HAS CHANGED")


                
        # Get a list of supported ranges and validate the range index.
            ranges = ai_info.get_ranges(input_mode)
            if range_index >= len(ranges):
                range_index = len(ranges) - 1

            print('\n', descriptor.dev_string, ' Connected and Ready', sep='')
          
            return ai_device, descriptor, input_mode, ranges, daq_device


        
    except RuntimeError as error:
        print('\n', error)

if __name__ == '__main__':
    # test1.py executed as scriptc
    # do something
    print("hello world")