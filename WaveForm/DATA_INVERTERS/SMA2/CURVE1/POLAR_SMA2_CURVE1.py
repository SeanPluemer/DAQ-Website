import numpy as np
import matplotlib.pylab as plt
from matplotlib.pyplot import figure, show, rc, grid

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
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW10.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_10[0] += [ang[y]]
            P_10[1] += [VA[y]]
    elif i==1:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW20.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_20[0] += [ang[y]]
            P_20[1] += [VA[y]]
    elif i==2:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW30.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_30[0] += [ang[y]]
            P_30[1] += [VA[y]]
    elif i==3:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW40.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_40[0] += [ang[y]]
            P_40[1] += [VA[y]]
    elif i==4:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW50.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_50[0] += [ang[y]]
            P_50[1] += [VA[y]]
    elif i==5:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW60.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_60[0] += [ang[y]]
            P_60[1] += [VA[y]]
    elif i==6:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW70.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_70[0] += [ang[y]]
            P_70[1] += [VA[y]] 
    elif i==7:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW80.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_80[0] += [ang[y]]
            P_80[1] += [VA[y]] 
    elif i==8:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW90.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_90[0] += [ang[y]]
            P_90[1] += [VA[y]] 
    elif i==9:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW100.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_100[0] += [ang[y]]
            P_100[1] += [VA[y]] 
    elif i==10:
        t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW110.csv',delimiter=',',unpack=True)
        for y in range(len(t)):
            P_110[0] += [ang[y]]
            P_110[1] += [VA[y]] 
    
    
            
    
        
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
plt.scatter(P_100[0], P_100[1], color='black', label='100% DC')
plt.scatter(P_110[0], P_110[1], color='green', label='110% DC')


pf = 0.85
ref_angle = np.arccos(pf)

vec1 = np.array([0,ref_angle])
vec2 = np.array([0,3000])

#ploting the pf limits 
plt.scatter(vec1,vec2,color='red',marker='.')
plt.plot(vec1,vec2,color='red',linewidth=3.0)
plt.scatter(-vec1,vec2,color='red',marker='.')
plt.plot(-vec1,vec2,color='red',linewidth=3.0)

#real axis
real_angle = np.array([0,np.pi])
real_mag = np.array([3000,3000])
plt.scatter(real_angle,real_mag,color='black',marker='.')
plt.plot(real_angle,real_mag,color='black',linewidth=2.0)

#reactive axis
react_angle = np.array([np.pi/2,-np.pi/2])
react_mag = np.array([3000,3000])
plt.scatter(react_angle,react_mag,color='black',marker='.')
plt.plot(react_angle,react_mag,color='black',linewidth=2.0)


ax.set_rmax(2500)
#plt.title('Inverter operation zones at different DC power levels')
#ax.set_title('Zones of operation of inverter', horizontalalignment='right', verticalalignment='top')
rc('grid', color='#316931', linewidth=1, linestyle='-')
rc('xtick', labelsize=30) 
rc('ytick', labelsize=30)
plt.legend(loc="center left",fontsize=22)
plt.show()


