import numpy as np
import matplotlib.pylab as plt
import matplotlib

############################################################################################################
def Fourier_transform(Volts,Vars):
    w = 2*np.pi
    N = len(Volts)                              # Vector length
    Fs = 1/(Volts[2]-Volts[1])                  # Samples per volt
    fr = Fs/N                                   # Frequency resolution
    
    FFT_VV = np.fft.fft(Vars,N)                 # FFT of volt/var curve
#    xfft = np.arange(0,len(FFT_VV))*fr
    
    N2 = int(N/2)
    FFT_VV2 = FFT_VV[0:N2]*2
#    xfft2 = xfft[0:N2]
    
    harmonics = [[],[],[],[]]                   # Most significant harmonics
    discrim = 0.5                               # Discrimination factor
    
    for i in range(0,N2):
        if np.abs(FFT_VV2[i]) >= discrim:
        #Current harmonic discrimination
            harmonics[0].append(i)
            harmonics[1].append(FFT_VV2[i]/N)
            harmonics[2].append(np.absolute(FFT_VV2[i])/N)
            harmonics[3].append(np.angle(FFT_VV2[i]))
 
    if harmonics[0][0] == 0:
        harmonics[1][0] = harmonics[1][0]/2
        harmonics[2][0] = np.absolute(harmonics[1][0])
        
    ### Recovery
    recover = []

    for i in range(len(Volts)):
        acum = 0.0
        for k in range(0,len(harmonics[0])):
            if harmonics[0][k] != 0:
                acum += harmonics[2][k]*np.cos(w*harmonics[0][k]*fr*Volts[i] + harmonics[3][k])
        if harmonics[0][0] == 0:
            acum += np.real(harmonics[1][0])
       
        recover += [acum]
    return recover
############################################################################################################
    
    
P_10 = [[],[]]
P_20 = [[],[]]
P_30 = [[],[]]
P_40 = [[],[]]
P_50 = [[],[]]
P_60 = [[],[]]
P_70 = [[],[]]
P_80 = [[],[]]
P_90 = [[],[]]
P_100 = [[],[]]
P_110 = [[],[]]

for i in range(11):
    if i==0:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW10.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_10[0] += [(Grid_Sim[y]+0.275)/100]
            P_10[1] += [React[y]/1600]
        recP_10 = Fourier_transform(P_10[0],P_10[1])
        plt.scatter(P_10[0],P_10[1],color='blue',label='10% of DC')
        plt.plot(P_10[0],recP_10,color='red',linewidth=2.0)
    elif i==1:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW20.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_20[0] += [(Grid_Sim[y]-0.1)/100]
            P_20[1] += [React[y]/1600]
        recP_20 = Fourier_transform(P_20[0],P_20[1])
        plt.scatter(P_20[0],P_20[1],color='yellow',label='10% of DC')
        plt.plot(P_20[0],recP_20,color='red',linewidth=2.0)
    elif i==2:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW30.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_30[0] += [(Grid_Sim[y]-0.1)/100]
            P_30[1] += [React[y]/1600]
        recP_30 = Fourier_transform(P_30[0],P_30[1])    
    elif i==3:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW40.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_40[0] += [(Grid_Sim[y]-0.1)/100]
            P_40[1] += [React[y]/1600]
        recP_40 = Fourier_transform(P_40[0],P_40[1])   
    elif i==4:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW50.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_50[0] += [(Grid_Sim[y]-0.1)/100]
            P_50[1] += [React[y]/1600]
        recP_50 = Fourier_transform(P_50[0],P_50[1])   
    elif i==5:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW60.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_60[0] += [(Grid_Sim[y]-0.1)/100]
            P_60[1] += [React[y]/1600]
        recP_60 = Fourier_transform(P_60[0],P_60[1])    
    elif i==6:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW70.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_70[0] += [(Grid_Sim[y]-0.1)/100]
            P_70[1] += [React[y]/1600]
        recP_70 = Fourier_transform(P_70[0],P_70[1])    
    elif i==7:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW80.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_80[0] += [(Grid_Sim[y]-0.1)/100]
            P_80[1] += [React[y]/1600]
        recP_80 = Fourier_transform(P_80[0],P_80[1])   
    elif i==8:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW90.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_90[0] += [(Grid_Sim[y]-0.1)/100]
            P_90[1] += [React[y]/1600]
        recP_90 = Fourier_transform(P_90[0],P_90[1])   
    elif i==9:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW100.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_100[0] += [(Grid_Sim[y]-0.1)/100]
            P_100[1] += [React[y]/1600]
        recP_100 = Fourier_transform(P_100[0],P_100[1])    
    elif i==10:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW110.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_110[0] += [(Grid_Sim[y]+0.275)/100]
            P_110[1] += [React[y]/1600]
        recP_110 = Fourier_transform(P_110[0],P_110[1])


plt.grid()
plt.xlabel('Voltage (p.u.)',fontsize=33)
plt.ylabel('Reactive Power (p.u.)',fontsize=33)
plt.xlim(0.90,1.10)
plt.legend(fontsize=20)
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)
#########################################################################################################

