try:
    import numpy as np
    from prettytable import PrettyTable
    #from matplotlib.mlab import find, this is outdated, just wrote find function below
    import matplotlib.pyplot as plt
    import numpy as np
    import math
    from scipy import signal
    import script

except Exception as e:
    print(e)  # This will appear in the SVP log file.
    
def calc_RMS(data):
    """
    :param data: list

    return:
    : rms - RMS of signal provided
    """
    rms = np.sqrt(np.mean((np.asarray(data))**2))
    return(rms)

def calc_power(V,I):
    """
    :param V: voltage vector (numpy)
    :param I: current vector (numpy)
    """
    pass
def active_power_from_waveform(t, V, I, sampling_rate, ts):
    """
    :param t: time vector (numpy)
    :param V: voltage vector (numpy)
    :param I: current vector (numpy)
    :param sampling_rate - sampling rate (int)
    :param ts - test script with logging capabilities

    :return:
    : avg_P - Average active power
    """
    pass


def reactive_power_from_waveform(t, V, I, sampling_rate, ts):
    """
    :param t: time vector (numpy)
    :param V: voltage vector (numpy)
    :param I: current vector (numpy)
    :param sampling_rate - sampling rate (int)
    :param ts - test script with logging capabilities

    :return:
    : Q1 - Fundamental Reactive Power
    """
    pass

import time
def pf_from_waveform(t, V, I, sample_rate):

    """
    :param t: time vector (numpy)
    :param V: voltage vector (numpy)
    :param I: current vector (numpy)
    :param sampling_rate - sampling rate (int)

    :return:
    : avg_P - Average active power
    : P1 - Fundamental active power
    : PH - Nonfundamental active power

    : N - Nonactive Power
    : Q1 - Fundamental Reactive Power
    : DI - Current distortion power
    : DV - Voltage distortion power
    : DH - Harmonic distortion power

    : S - Combined Apparent Power
    : S1 - Fundamental Apparent Power
    : SN - Nonfundamental Apparent Power
    : SH - Harmonic Apparent power

    : PF1 - Fundamental power factor
    : PF - Power factor

    : har_poll - Harmonic pollution

    : THD_V - Voltage Total Harmonic Distortion
    : THD_I - Current Total Harmonic Distortion
    """
    P = V*I

    w = 2*np.pi
    Fs = 1000 #TODO I am not sure why this 
    #print(Fs) 

    print(len(t), len(V), len(I)) 
    if 0 in V: 
        print("zero!")
    if 0 in I: 
        print("Izero!")
    ffI = np.fft.fft(I, len(t))


    ffV = np.fft.fft(V, len(t))
    xfft = np.arange(0, len(ffI))*(Fs/len(ffI))

    ffI2 = ffI[0:500]
    ffV2 = ffV[0:500]
    xfft2 = xfft[0:500]
    

    # lists with harmonic content harmonicsVI = [[n],[complex/norm],[abs/norm],[phase]] = [[0],[1],[2],[3]]
    # [0] = n
    # [1] = complex/norm
    # [2] = abs/norm
    # [3] = phase

    harmonicsI = [[], [], [], []]
    harmonicsV = [[], [], [], []]
    powers = [[], [], []]
    recoverI = []
    recoverV = []
      
    for i in range(len(ffI2)):
        if abs(ffI2[i]) >= 0.15:
            harmonicsI[0] += [i]
            harmonicsI[1] += [ffI2[i]*2/len(ffI)]
            harmonicsI[2] += [abs(ffI2[i])*2/len(ffI)]
            harmonicsI[3] += [np.angle(ffI2[i])]

            harmonicsV[0] += [i]
            harmonicsV[1] += [ffV2[i]*2/len(ffV)]
            harmonicsV[2] += [abs(ffV2[i])*2/len(ffV)]
            harmonicsV[3] += [np.angle(ffV2[i])]

    harmonicsI[1][0] = harmonicsI[1][0]/2
    harmonicsI[2][0] = abs(np.real(harmonicsI[1][0]))
    harmonicsV[1][0] = harmonicsV[1][0]/2
    harmonicsV[2][0] = abs(np.real(harmonicsV[1][0]))

    # synthesis
    for i in range(len(t)):
        acumI = 0.0
        acumV = 0.0
        for k in range(1,len(harmonicsI[0])):
            acumI += harmonicsI[2][k]*np.sin(w*harmonicsI[0][k]*(Fs/len(ffI))*t[i] + harmonicsI[3][k] + (np.pi)/2)
            acumV += harmonicsV[2][k]*np.sin(w*harmonicsV[0][k]*(Fs/len(ffV))*t[i] + harmonicsV[3][k] + (np.pi)/2)
        acumI += np.real(harmonicsI[1][0])
        acumV += np.real(harmonicsV[1][0])
        recoverI += [acumI]
        recoverV += [acumV]
        print(i)


    ###############################################################################
    ################ CALCULATIONS ACCORDING TO IEEE 1459 ##########################
    ###############################################################################

    #THD = VH/V1
    VHsq = 0.0
    IHsq = 0.0
    V0sq = 0.0
    I0sq = 0.0
    V1sq = 0.0
    I1sq = 0.0


    for i in range(len(harmonicsV[0])):
        if harmonicsV[0][i]==0:
            #THDs
            V0sq = np.square(harmonicsV[2][i])
            I0sq = np.square(harmonicsI[2][i])
            VHsq += V0sq
            IHsq += I0sq
            #harmonics power
            powers[0] += [harmonicsI[0][i]*(Fs/len(I))/60.0]
            powers[1] += [np.real(harmonicsI[1][i])*np.real(harmonicsV[1][i])]
            powers[2] += [0]

        elif harmonicsV[0][i]*Fs/len(t)==60:
            #THDs
            V1sq = np.square(harmonicsV[2][i])/2
            I1sq = np.square(harmonicsI[2][i])/2
            VHsq += 0.0
            IHsq += 0.0
            #harmonics power
            powers[0] += [harmonicsI[0][i]*(Fs/len(I))/60.0]
            powers[1] += [harmonicsI[2][i]*harmonicsV[2][i]*np.cos(harmonicsI[3][i]-harmonicsV[3][i])/2]
            powers[2] += [harmonicsI[2][i]*harmonicsV[2][i]*np.sin(harmonicsI[3][i]-harmonicsV[3][i])/2]

        else:
            #THDs
            VHsq += np.square(harmonicsV[2][i])/2
            IHsq += np.square(harmonicsI[2][i])/2
            #harmonics power
            powers[0] += [harmonicsI[0][i]*(Fs/len(I))/60.0]
            powers[1] += [harmonicsI[2][i]*harmonicsV[2][i]*np.cos(harmonicsI[3][i]-harmonicsV[3][i])/2]
            powers[2] += [0]



    Vsq = V1sq+VHsq
    Isq = I1sq+IHsq

    THD_I = np.sqrt(IHsq/I1sq)
    THD_V = np.sqrt(VHsq/V1sq)

    THD_I2 = np.sqrt((Isq/I1sq)-1)
    THD_V2 = np.sqrt((Vsq/V1sq)-1)
    #instantaneous power
    i_P = 0.0
    for i in range(len(P)):
        i_P += P[i]

    avg_P = i_P/len(P)
    avg_P2 = np.mean(P)

    #plt.plot(t,P)
    PH = 0.0
    P1 = 0.0

    for i in range(len(powers[0])):
        if powers[0][i] == 1:
            P1 = powers[1][i]
            Q1 = powers[2][i]
        else:
            PH += powers[1][i]


    #Fundamental Apparent Power
    S1 = np.sqrt(np.square(P1)+np.square(Q1))

    #Current distortion power
    DI = S1*THD_I
    DI_2 = np.sqrt(V1sq)*(np.sqrt(Isq-I1sq))

    #Voltage distortion power
    DV = S1*THD_V
    DV_2 = np.sqrt(Vsq-V1sq)*np.sqrt(I1sq)

    #Harmonic Apparent power
    SH = S1*THD_I*THD_V
    SH_2 = (np.sqrt(Isq-I1sq))*np.sqrt(Vsq-V1sq)

    #Harmonic distortion power
    DH = np.sqrt(np.square(SH)-np.square(PH))

    #Nonfundamental Apparent Power
    SN = np.sqrt(np.square(DI) + np.square(DV) + np.square(SH))
    S = np.sqrt(np.square(S1)+np.square(SN))

    #Nonactive Power
    N = np.sqrt(np.square(S)-np.square(avg_P))

    #Fundamental power factor
    PF1 = P1/S1

    #Power factor
    PF = avg_P/S

    #Harmonic pollution
    har_poll = SN/S1
    print("hello")

    return avg_P, P1, PH, N, Q1, DI, DV, S, S1, SN, SH, PF1, PF, har_poll,  THD_V, THD_I

def temp_calc(rmsV,rmsI,V,I):
    S = rmsV*rmsI 
    P = V*I
    i_P = 0.0
    for i in range(len(P)):
        i_P += P[i]

    avg_P = i_P/len(P)
    PF = avg_P/S

    return S,PF, avg_P


if __name__ == "__main__":
    print("Run_a_in.py was run directly for some reason?")
    main()