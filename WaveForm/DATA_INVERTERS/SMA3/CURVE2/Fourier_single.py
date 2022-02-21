import numpy as np
import matplotlib.pylab as plt
import matplotlib

V,Vars = np.loadtxt(r'c:\DATA_INVERTERS\SMA3\CURVE2\POW10_FFT.csv',delimiter=',',unpack=True)

V=V/100
w = 2*np.pi
max_vars = 1600
Vars = Vars/max_vars
Fs = 1/(V[2]-V[1])                          # Samples per volt
N = len(V)                                  # Number of samples
FFT_VV = np.fft.fft(Vars,N)                 # FFT of volt/var curve
fr = Fs/N                                   # Frequency resolution
xfft = np.arange(0,len(FFT_VV))*fr

N2 = int(N/2)
FFT_VV2 = FFT_VV[0:N2]*2
xfft2 = xfft[0:N2]

'''plt.stem(xfft2,np.absolute(FFT_VV2))
plt.grid()
plt.legend()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude of FFT')'''


harmonics = [[],[],[],[]]                   # Most significant harmonics
discrim = 0.5

#harmonics = [[n],[complex],[abs],[phase]]
#n = sample number (frequency bin)
#complex = complex value of Fourier coefficient "n"
#abs = magnitude value of Fourier coefficient "n"
#phase = angle (rads) of Fourier coefficient "n"

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

for i in range(len(V)):
    acum = 0.0
    for k in range(0,len(harmonics[0])):
        if harmonics[0][k] != 0:
            acum += harmonics[2][k]*np.cos(w*harmonics[0][k]*fr*V[i] + harmonics[3][k])
    if harmonics[0][0] == 0:
       acum += np.real(harmonics[1][0])
       
    recover += [acum]

    
plt.plot(V-0.275/100,recover,color='red',linewidth=2.0,label='Fourier (Fundamental + 146 Harmonics)')     
plt.scatter(V,Vars,color='blue',label='Experimental data') 
plt.grid()
plt.xlabel('Voltage (p.u.)',fontsize=33)
plt.ylabel('Reactive Power (p.u.)',fontsize=33)
plt.xlim(0.90,1.10)
plt.legend(fontsize=20)
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)
    
    
    
    
    
    