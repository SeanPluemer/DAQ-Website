import numpy as np
import matplotlib.pylab as plt

P10 = [[],[],[],[]]
P20 = [[],[],[],[]]
P30 = [[],[],[],[]]
P40 = [[],[],[],[]]
P50 = [[],[],[],[]]
P60 = [[],[],[],[]]
P70 = [[],[],[],[]]
P80 = [[],[],[],[]]
P90 = [[],[],[],[]]
P100 = [[],[],[],[]]
P110 = [[],[],[],[]]

#curve 1
volts = np.array([213,220.8,232.8,247.2,259.2,264])
vars = np.array([1600,1600,0,0,-1600,-1600])

for i in range(10):
    if i==0:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_10.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW10.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P10[0] += [AC_Voltage[y]/240*100]
            P10[1] += [React[y]/1600*100]
            P10[2] += [AC_Voltage2[y]/240*100]
            P10[3] += [React2[y]/1600*100]
    if i==1:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_20.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW20.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P20[0] += [AC_Voltage[y]/240*100]
            P20[1] += [React[y]/1600*100]
            P20[2] += [AC_Voltage2[y]/240*100]
            P20[3] += [React2[y]/1600*100]
    if i==2:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_30.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW30.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P30[0] += [AC_Voltage[y]/240*100]
            P30[1] += [React[y]/1600*100]
            P30[2] += [AC_Voltage2[y]/240*100]
            P30[3] += [React2[y]/1600*100]
    if i==3:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_40.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW40.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P40[0] += [AC_Voltage[y]/240*100]
            P40[1] += [React[y]/1600*100]
            P40[2] += [AC_Voltage2[y]/240*100]
            P40[3] += [React2[y]/1600*100]
    if i==4:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_50.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW50.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P50[0] += [AC_Voltage[y]/240*100]
            P50[1] += [React[y]/1600*100]
            P50[2] += [AC_Voltage2[y]/240*100]
            P50[3] += [React2[y]/1600*100]
    if i==5:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_60.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW60.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P60[0] += [AC_Voltage[y]/240*100]
            P60[1] += [React[y]/1600*100]
            P60[2] += [AC_Voltage2[y]/240*100]
            P60[3] += [React2[y]/1600*100]
    if i==6:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_70.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW70.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P70[0] += [AC_Voltage[y]/240*100]
            P70[1] += [React[y]/1600*100]
            P70[2] += [AC_Voltage2[y]/240*100]
            P70[3] += [React2[y]/1600*100]
    if i==7:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_80.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW80.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P80[0] += [AC_Voltage[y]/240*100]
            P80[1] += [React[y]/1600*100]
            P80[2] += [AC_Voltage2[y]/240*100]
            P80[3] += [React2[y]/1600*100]
    if i==8:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_90.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW90.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P90[0] += [AC_Voltage[y]/240*100]
            P90[1] += [React[y]/1600*100]
            P90[2] += [AC_Voltage2[y]/240*100]
            P90[3] += [React2[y]/1600*100]
    if i==9:
        t,DC_Available,DC_Power,AC_Voltage,React,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set1\CURVE1\P_100.csv',delimiter=',',unpack=True)
        t2,DC_Available2,DC_Power2,AC_Voltage2,React2,Real2,Grid_Sim2,ang2,VA2 = np.loadtxt('c:\DATA_INVERTERS\VV_SWEEPS\set2\CURVE1\POW100.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P100[0] += [AC_Voltage[y]/240*100]
            P100[1] += [React[y]/1600*100]
            P100[2] += [AC_Voltage2[y]/240*100]
            P100[3] += [React2[y]/1600*100]
            

            
print('DC power percentage?')
res = input()
           
if res==str(10):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P10[0],P10[1],color='red',label='First Set')
    plt.scatter(P10[2],P10[3],color='green',label='Second Set') 
    plt.title('10% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(20):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P20[0],P20[1],color='red',label='First Set')
    plt.scatter(P20[2],P20[3],color='yellow',label='Second Set') 
    plt.title('20% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(30):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P30[0],P30[1],color='red',label='First Set')
    plt.scatter(P30[2],P30[3],color='yellow',label='Second Set') 
    plt.title('30% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(40):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P40[0],P40[1],color='red',label='First Set')
    plt.scatter(P40[2],P40[3],color='yellow',label='Second Set') 
    plt.title('40% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(50):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P50[0],P50[1],color='red',label='First Set')
    plt.scatter(P50[2],P50[3],color='yellow',label='Second Set') 
    plt.title('50% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(60):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P60[0],P60[1],color='red',label='First Set')
    plt.scatter(P60[2],P60[3],color='yellow',label='Second Set') 
    plt.title('60% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(70):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P70[0],P70[1],color='red',label='First Set')
    plt.scatter(P70[2],P70[3],color='yellow',label='Second Set') 
    plt.title('70% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(80):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P80[0],P80[1],color='red',label='First Set')
    plt.scatter(P80[2],P80[3],color='yellow',label='Second Set') 
    plt.title('80% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(90):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P90[0],P90[1],color='red',label='First Set')
    plt.scatter(P90[2],P90[3],color='yellow',label='Second Set') 
    plt.title('90% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
if res==str(100):
    plt.plot(volts/240.*100.,vars/1600.*100.,color='blue',label='curve1')    
    plt.scatter(P100[0],P100[1],color='red',label='First Set')
    plt.scatter(P100[2],P100[3],color='yellow',label='Second Set') 
    plt.title('100% of DC POWER')
    plt.xlabel('Grid Simulator Voltage (Vac p.u.)')
    plt.ylabel('Reactive Power (% nameplate)')
    plt.ylim(-110,110)
    plt.grid()
    plt.legend()
