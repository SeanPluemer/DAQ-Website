from __future__ import division
from numpy import logical_and, average, diff
from matplotlib.mlab import find
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import math
import rt_analysis

__author__ = 'detldaq'


if __name__ == "__main__":

    import sandia_dsm as dsm
    wfmtrigger = dsm.WfmTrigger(ts=None)

    # get data from waveform saved on the hard drive
    # (this function could use a little help to make it more robust...)
    wfmname = wfmtrigger.getfilename()
    print('Analyzing waveform data in file "%s".' % wfmname)
    wfmtime, ac_voltage, ac_current, grid_trig = wfmtrigger.read_file(wfmname)

    # Determine if the inverter shut off (current dropped to < 5% of nameplate)

    # if current remains: return 0 for no trip/cease to energize time

    # if ceasing to energize: determine time of current drop [t_current_small - grid sim trigger time]

    # and determine time before current output returned
    # [if "trip" it should take ~25 seconds, if "cease to energize it should take ~2 seconds to return]

    if wfmname[14] == 'V':
        thresh = [0.993,0.97,0.9]
        trip_time, return_time = rt_analysis.volt_trip(wfmtime, ac_voltage, ac_current, grid_trig,24*10**3,1,thresh)
    else:
        thresh = [0.993,0.97,0.9]
        trip_time, return_time = rt_analysis.freq_trip(wfmtime, ac_voltage, ac_current, grid_trig,24*10**3,1,thresh)

    ride_through_time,service_return_time = rt_analysis.ride_through(wfmtime, ac_voltage, ac_current, grid_trig,24*10**3,1,thresh,trip_time)

    print "Trip Time = %s, Trip Return Time = %s" %(trip_time,return_time)
    print "Ride Through Time = %s, Service Return Time = %s" %(ride_through_time,service_return_time)

    #ride_through_time = calc_ride_through_duration(wfmtime, ac_current, ac_voltage=ac_voltage, grid_trig=grid_trig)
    #ride_through_time = calc_ride_through_duration(wfmtime, ac_current, grid_trig=grid_trig)



    '''
    plt.plot(wfmtime, ac_voltage, color='blue', label='ac_voltage data')
    plt.plot(wfmtime, ac_current, color='red', label='ac_current')
    plt.plot(wfmtime, grid_trig, 'g', label='grid_trig')
    plt.grid(which='both', axis='both')
    plt.show()

    plt.plot(wfmtime, grid_trig, 'g', label='grid_trig')
    plt.grid(which='both', axis='both')
    plt.show()

    fs = 24e3
    avg_frequency, frequencies = freq_from_crossings(wfmtime, ac_voltage, fs)
    #print frequencies

    cycles_in_window = 5.
    f_grid = 60.
    windowSize = cycles_in_window*(1./f_grid)*1000.  # in ms
    time_RMS, ac_voltage_RMS = calculateRmsOfSignal(ac_voltage, windowSize=windowSize, samplingFrequency=fs,
                                                    overlap=windowSize/3)

    wn = (2.*math.pi*60.)/fs  #Wn is normalized from 0 to 1, where 1 is the Nyquist frequency, pi radians/sample
    b, a = signal.butter(4, wn, analog=False)
    sig_ff = signal.filtfilt(b, a, ac_voltage)
    time_filt_RMS, ac_voltage_filt_RMS = calculateRmsOfSignal(sig_ff, windowSize=windowSize,
                                                              samplingFrequency=fs, overlap=windowSize/3)

    print ac_voltage_filt_RMS
    print ac_voltage_RMS

    plt.plot(wfmtime, ac_voltage, color='red', label='Voltage')
    plt.plot(time_RMS, ac_voltage_RMS, color='black', label='Voltage_RMS')
    plt.plot(wfmtime, sig_ff, color='green', label='Voltage Filtered')
    plt.plot(time_filt_RMS, ac_voltage_filt_RMS, color='blue', label='Filtered Voltage_RMS')
    plt.legend()
    plt.grid(which='both', axis='both')
    plt.show()
    '''
