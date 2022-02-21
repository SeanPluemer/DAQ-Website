import numpy as np
import matplotlib.pylab as plt
import matplotlib

P_10 = [[],[],[],[],[],[],[],[],[],[]]
P_20 = [[],[],[],[],[],[],[],[],[],[]]
P_30 = [[],[],[],[],[],[],[],[],[],[]]
P_40 = [[],[],[],[],[],[],[],[],[],[]]
P_50 = [[],[],[],[],[],[],[],[],[],[]]
P_60 = [[],[],[],[],[],[],[],[],[],[]]
P_70 = [[],[],[],[],[],[],[],[],[],[]]
P_80 = [[],[],[],[],[],[],[],[],[],[]]
P_90 = [[],[],[],[],[],[],[],[],[],[]]
P_100 = [[],[],[],[],[],[],[],[],[],[]]
P_110 = [[],[],[],[],[],[],[],[],[],[]]

for i in range(11):
    if i==0:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW10.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_10[0] += [t[y]]
            P_10[1] += [DC_Available[y]]
            P_10[2] += [DC_Power[y]]
            P_10[3] += [AC_Voltage[y]/240]
            P_10[4] += [React[y]/1600]
            P_10[5] += [Nonactive[y]]
            P_10[6] += [Real[y]]
            P_10[7] += [Grid_Sim[y]]
            P_10[8] += [ang[y]]
            P_10[9] += [VA[y]]
    elif i==1:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW20.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_20[0] += [t[y]]
            P_20[1] += [DC_Available[y]]
            P_20[2] += [DC_Power[y]]
            P_20[3] += [AC_Voltage[y]/240]
            P_20[4] += [React[y]/1600]
            P_20[5] += [Nonactive[y]]
            P_20[6] += [Real[y]]
            P_20[7] += [Grid_Sim[y]]
            P_20[8] += [ang[y]]
            P_20[9] += [VA[y]]
    elif i==2:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW30.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_30[0] += [t[y]]
            P_30[1] += [DC_Available[y]]
            P_30[2] += [DC_Power[y]]
            P_30[3] += [AC_Voltage[y]/240]
            P_30[4] += [React[y]/1600]
            P_30[5] += [Nonactive[y]]
            P_30[6] += [Real[y]]
            P_30[7] += [Grid_Sim[y]]
            P_30[8] += [ang[y]]
            P_30[9] += [VA[y]]
    elif i==3:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW40.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_40[0] += [t[y]]
            P_40[1] += [DC_Available[y]]
            P_40[2] += [DC_Power[y]]
            P_40[3] += [AC_Voltage[y]/240]
            P_40[4] += [React[y]/1600]
            P_40[5] += [Nonactive[y]]
            P_40[6] += [Real[y]]
            P_40[7] += [Grid_Sim[y]]
            P_40[8] += [ang[y]]
            P_40[9] += [VA[y]]
    elif i==4:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW50.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_50[0] += [t[y]]
            P_50[1] += [DC_Available[y]]
            P_50[2] += [DC_Power[y]]
            P_50[3] += [AC_Voltage[y]/240]
            P_50[4] += [React[y]/1600]
            P_50[5] += [Nonactive[y]]
            P_50[6] += [Real[y]]
            P_50[7] += [Grid_Sim[y]]
            P_50[8] += [ang[y]]
            P_50[9] += [VA[y]]
    elif i==5:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW60.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_60[0] += [t[y]]
            P_60[1] += [DC_Available[y]]
            P_60[2] += [DC_Power[y]]
            P_60[3] += [AC_Voltage[y]/240]
            P_60[4] += [React[y]/1600]
            P_60[5] += [Nonactive[y]]
            P_60[6] += [Real[y]]
            P_60[7] += [Grid_Sim[y]]
            P_60[8] += [ang[y]]
            P_60[9] += [VA[y]]
    elif i==6:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW70.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_70[0] += [t[y]]
            P_70[1] += [DC_Available[y]]
            P_70[2] += [DC_Power[y]]
            P_70[3] += [AC_Voltage[y]/240]
            P_70[4] += [React[y]/1600]
            P_70[5] += [Nonactive[y]]
            P_70[6] += [Real[y]]
            P_70[7] += [Grid_Sim[y]]
            P_70[8] += [ang[y]]
            P_70[9] += [VA[y]]
    elif i==7:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW80.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_80[0] += [t[y]]
            P_80[1] += [DC_Available[y]]
            P_80[2] += [DC_Power[y]]
            P_80[3] += [AC_Voltage[y]/240]
            P_80[4] += [React[y]/1600]
            P_80[5] += [Nonactive[y]]
            P_80[6] += [Real[y]]
            P_80[7] += [Grid_Sim[y]]
            P_80[8] += [ang[y]]
            P_80[9] += [VA[y]]
    elif i==8:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW90.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_90[0] += [t[y]]
            P_90[1] += [DC_Available[y]]
            P_90[2] += [DC_Power[y]]
            P_90[3] += [AC_Voltage[y]/240]
            P_90[4] += [React[y]/1600]
            P_90[5] += [Nonactive[y]]
            P_90[6] += [Real[y]]
            P_90[7] += [Grid_Sim[y]]
            P_90[8] += [ang[y]]
            P_90[9] += [VA[y]]
    elif i==9:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW100.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_100[0] += [t[y]]
            P_100[1] += [DC_Available[y]]
            P_100[2] += [DC_Power[y]]
            P_100[3] += [AC_Voltage[y]/240]
            P_100[4] += [React[y]/1600]
            P_100[5] += [Nonactive[y]]
            P_100[6] += [Real[y]]
            P_100[7] += [Grid_Sim[y]]
            P_100[8] += [ang[y]]
            P_100[9] += [VA[y]]
    elif i==10:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE2\POW110.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_110[0] += [t[y]]
            P_110[1] += [DC_Available[y]]
            P_110[2] += [DC_Power[y]]
            P_110[3] += [AC_Voltage[y]/240]
            P_110[4] += [React[y]/1600]
            P_110[5] += [Nonactive[y]]
            P_110[6] += [Real[y]]
            P_110[7] += [Grid_Sim[y]]
            P_110[8] += [ang[y]]
            P_110[9] += [VA[y]]
 
            
CURVE2_volts = np.array([213,228,237.6,242.4,252,264])
CURVE2_vars = np.array([1600,1600,0,0,-1600,-1600])

#ploting
size_marker=10
plt.plot(CURVE2_volts/240,CURVE2_vars/1600,color='black',linewidth=4.0,label='Programmed function 2')
matplotlib.rc('xtick', labelsize=30) 
matplotlib.rc('ytick', labelsize=30)
plt.scatter(P_10[3],P_10[4],color='chartreuse',label='10% of DC Power',s=size_marker)
plt.scatter(P_20[3],P_20[4],color='blue',label='20% of DC Power',s=size_marker)
plt.scatter(P_30[3],P_30[4],color='green',label='30% of DC Power',s=size_marker)
plt.scatter(P_40[3],P_40[4],color='yellow',label='40% of DC Power',s=size_marker)
plt.scatter(P_50[3],P_50[4],color='brown',label='50% of DC Power',s=size_marker)
plt.scatter(P_60[3],P_60[4],color='cyan',label='60% of DC Power',s=size_marker)
plt.scatter(P_70[3],P_70[4],color='magenta',label='70% of DC Power',s=size_marker)
plt.scatter(P_80[3],P_80[4],color='red',label='80% of DC Power',s=size_marker)
plt.scatter(P_90[3],P_90[4],color='k',label='90% of DC Power',s=size_marker)
plt.scatter(P_100[3],P_100[4],color='purple',label='100% of DC Power',s=size_marker)
plt.scatter(P_110[3],P_110[4],color='orange',label='110% of DC Power',s=size_marker)


plt.legend(fontsize=20)
plt.grid()
#plt.title('Volt/Var curves for device #2',fontsize=22,fontweight='bold')
plt.xlabel('Grid Simulator Voltage (Vac p.u.)',fontsize=33)
plt.ylabel('Reactive Power (%nameplate)',fontsize=33)
plt.ylim(-1.1,1.1)

