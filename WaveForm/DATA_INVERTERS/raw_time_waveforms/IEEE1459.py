import numpy as np
import matplotlib.pylab as plt
from prettytable import PrettyTable

t,V,I = np.loadtxt(r'c:\DATA_INVERTERS\raw_time_waveforms\SMA_Node_10_1.csv',delimiter=',',unpack=True)

P = V*I
w=2*np.pi

Fs = 10000
ffI = np.fft.fft(I,len(t))
ffV = np.fft.fft(V,len(t))
xfft = np.arange(0,len(ffI))*(Fs/len(ffI))

ffI2 = ffI[0:500]
ffV2 = ffV[0:500]
xfft2 = xfft[0:500]

# Plot harminocs of current and voltage

plt.subplot(4,1,2)
plt.plot(xfft2,abs(ffI2)*2/len(ffI),label='current harmonics')
plt.grid()
plt.legend()
plt.subplot(4,1,4)
plt.plot(xfft2,abs(ffV2)*2/len(ffV),label='voltage harmonics')
plt.grid()
plt.legend()
plt.show()

#lists with harmonic content harmonicsVI = [[n],[complex/norm],[abs/norm],[phase]] = [[0],[1],[2],[3]]
# [0] = n
# [1] = complex/norm
# [2] = abs/norm
# [3] = phase

harmonicsI = [[],[],[],[]]
harmonicsV = [[],[],[],[]]
powers = [[],[],[]]
recoverI = []
recoverV = []

for i in range(len(ffI2)):
    if abs(ffI2[i]) >= 3:
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
    
plt.subplot(4,1,1)
plt.plot(t,I,label='original')
plt.plot(t,recoverI,label='recovered')
plt.xlim(0,0.1)
plt.grid()
plt.legend()

plt.subplot(4,1,3)
plt.plot(t,V,label='original')
plt.plot(t,recoverV,label='recovered')
plt.xlim(0,0.1)
plt.grid()
plt.legend()
plt.show()

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
S1 = round(np.sqrt(np.square(P1)+np.square(Q1)),2)

#Nonfundamental Apparent Power

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

#Show results

x = PrettyTable()
x.field_names = ["Quantity or indicator","Combined","Fundamental Powers","Nonfundamental Powers"]
x.add_row(["Apparent","S = "+repr(S),"S1 = "+repr(S1),"SN = "+repr(SN)])
x.add_row(["","","","SH = "+repr(SH)])
x.add_row(["----------------------","------------------------","------------------------","----------------------------"])
x.add_row(["Active","P = "+repr(avg_P),"P1 = "+repr(P1),"PH = "+repr(PH)])
x.add_row(["----------------------","------------------------","------------------------","----------------------------"])
x.add_row(["Nonactive","N = "+repr(N),"Q1 = "+repr(Q1),"DI = "+repr(DI)])
x.add_row(["","","","DV = "+repr(DV)])
x.add_row(["","","","DH = "+repr(DH)])
x.add_row(["----------------------","------------------------","------------------------","----------------------------"])
x.add_row(["Line Utilization","PF = "+repr(PF),"PF1 = "+repr(PF1),"--------"])
x.add_row(["----------------------","------------------------","------------------------","----------------------------"])
x.add_row(["Harmonic Pollution","--------","--------","SN/S1 = "+repr(har_poll)])

print(x)


