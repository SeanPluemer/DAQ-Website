import numpy as np
import matplotlib.pylab as plt
import matplotlib


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

deltas = []

for i in range(11):
    if i==0:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW10.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_10[0] += [AC_Voltage[y]]
            P_10[1] += [React[y]]
       
    elif i==1:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW20.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_20[0] += [AC_Voltage[y]]
            P_20[1] += [React[y]]
       
    elif i==2:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW30.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_30[0] += [AC_Voltage[y]]
            P_30[1] += [React[y]]
           
    elif i==3:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW40.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_40[0] += [AC_Voltage[y]]
            P_40[1] += [React[y]]
           
    elif i==4:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW50.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_50[0] += [AC_Voltage[y]]
            P_50[1] += [React[y]]
           
    elif i==5:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW60.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_60[0] += [AC_Voltage[y]]
            P_60[1] += [React[y]]
            
    elif i==6:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW70.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_70[0] += [AC_Voltage[y]]
            P_70[1] += [React[y]]
            
    elif i==7:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW80.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_80[0] += [AC_Voltage[y]]
            P_80[1] += [React[y]]
           
    elif i==8:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW90.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_90[0] += [AC_Voltage[y]]
            P_90[1] += [React[y]]
           
    elif i==9:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW100.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_100[0] += [AC_Voltage[y]]
            P_100[1] += [React[y]]
          
    elif i==10:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA3\CURVE2\POW110.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_110[0] += [AC_Voltage[y]]
            P_110[1] += [React[y]]
       
plt.scatter(P_100[0],P_100[1])
plt.grid()
deltas += [0]
indicator = 2

P1 = [[0],[P_100[0][0]],[P_100[1][0]]]
P2 = [[],[],[]]
P3 = [[],[],[]]
P4 = [[],[],[]]
P5 = [[],[],[]]
P6 = [[len(P_100[0])-1],[P_100[0][len(P_100[0])-1]],[P_100[1][len(P_100[1])-1]]]

for i in range(1,len(P_100[1])):
    deltas += [np.absolute(P_100[1][i]-P_100[1][i-1])]
    if deltas[i] > 10 and indicator == 2:
        P2[0] += [i-1]
        P2[1] += [P_100[0][i-1]]
        P2[2] += [P_100[1][i-1]]
        indicator = 3
    elif deltas[i] < 10 and indicator == 3:
        P3[0] += [i-1]
        P3[1] += [P_100[0][i-1]]
        P3[2] += [P_100[1][i-1]]
        indicator = 4
    elif deltas[i] > 10 and indicator == 4:
        P4[0] += [i-1]
        P4[1] += [P_100[0][i-1]]
        P4[2] += [P_100[1][i-1]]
        indicator = 5
    elif deltas[i] < 10 and indicator == 5:
        P5[0] += [i-1]
        P5[1] += [P_100[0][i-1]]
        P5[2] += [P_100[1][i-1]]
        indicator = 6
