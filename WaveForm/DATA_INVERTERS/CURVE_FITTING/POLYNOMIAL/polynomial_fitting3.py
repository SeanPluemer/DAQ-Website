######################################################################
############## Polynomial regression analysis ########################
######################################################################

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


for i in range(11):
    t,DC_Available,DC_Power,AC_Voltage,React,Nonactive,Real,Grid_Sim,ang,VA = np.loadtxt('c:\DATA_INVERTERS\SMA2\CURVE1\POW'+str(i+1)+'0.csv',delimiter=',',unpack=True)
#    for y in range(len(t)):
#        'P_'+str(i+1)+'0[0]' += [AC_Voltage[y]/240]
#        'P_'+str(i+1)+'0[1]' += [React[y]/1600]
    
            

'''print('Give the irradiance % level you want to plot (10,20...110): ')            
irradiance = input()
print('Give the order of the polynomial (integer): ')
order_poly = input()
            
x = np.array(eval('P_'+irradiance+'[0]'))-1
y = np.array(eval('P_'+irradiance+'[1]'))

p = np.polyfit(x,y,int(order_poly))
f = np.poly1d(p)

size_marker=10 
size_marker2=1
plt.grid()

for i in range(len(x)):
    plt.xlim(-0.15,0.15)
    plt.ylim(-1.5,1.5)
    plt.scatter(x[i],y[i],color='red',label=irradiance +'% of DC Power (inverter data)',s=size_marker) 
    plt.plot(x[i],f(x[i]), label='Polynomial regression approximation model', color='blue')
    plt.pause(0.03)
    if i==0:
        plt.legend()
        
plt.plot(x,f(x), color='blue')'''





            
            
            
            
            
            
            