import numpy as np
import matplotlib.pylab as plt

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


for i in range(10):
    if i==0:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_10.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_10[0] += [ang[y]]
            P_10[1] += [VA[y]]
    elif i==1:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_20.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_20[0] += [ang[y]]
            P_20[1] += [VA[y]]
    elif i==2:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_30.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_30[0] += [ang[y]]
            P_30[1] += [VA[y]]
    elif i==3:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_40.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_40[0] += [ang[y]]
            P_40[1] += [VA[y]]
    elif i==4:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_50.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_50[0] += [ang[y]]
            P_50[1] += [VA[y]]
    elif i==5:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_60.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_60[0] += [ang[y]]
            P_60[1] += [VA[y]]
    elif i==6:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_70.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_70[0] += [ang[y]]
            P_70[1] += [VA[y]] 
    elif i==7:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_80.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_80[0] += [ang[y]]
            P_80[1] += [VA[y]] 
    elif i==8:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_90.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_90[0] += [ang[y]]
            P_90[1] += [VA[y]] 
    elif i==9:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_100.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_100[0] += [ang[y]]
            P_100[1] += [VA[y]] 
            
    
        
ax = plt.subplot(111, polar=True)
plt.scatter(P_10[0], P_10[1], color='red', label='10% DC')
plt.scatter(P_20[0], P_20[1], color='green', label='20% DC')
plt.scatter(P_30[0], P_30[1], color='purple', label='30% DC')
plt.scatter(P_40[0], P_40[1], color='yellow', label='40% DC')
plt.scatter(P_50[0], P_50[1], color='blue', label='50% DC')
plt.scatter(P_60[0], P_60[1], color='pink', label='60% DC')
plt.scatter(P_70[0], P_70[1], color='brown', label='70% DC')
plt.scatter(P_80[0], P_80[1], color='turquoise', label='80% DC')
plt.scatter(P_90[0], P_90[1], color='magenta', label='90% DC')
plt.scatter(P_100[0], P_100[1], color='black', label='90% DC')


plt.legend(loc="center left")
plt.show()
