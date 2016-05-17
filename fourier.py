import numpy as np
from scipy import signal
import matplotlib.pyplot as pl
pl.ion()

n = 100000
t = np.linspace(0., 20*np.pi, n)

y1 = np.sin(t) + np.sin(4.*t)
y2 = np.sin(t) + np.sin(4.*t) + 2./(20.*np.pi)*t
y2d = signal.detrend(y2)

def plot_spectrum(y, nfig):
    yfft = np.fft.rfft(y)
    yfft /= n
    yfft[1:-1] *= 2.
    
    pl.figure(nfig)
    pl.subplot(211)
    pl.plot(t, y)
    pl.subplot(212)
    pl.semilogx(abs(yfft))

plot_spectrum(y1 , 1)
plot_spectrum(y2 , 1)
plot_spectrum(y2d, 1)

y3 = np.sin(t)
y4 = np.cos(t)

plot_spectrum(y3, 2)
plot_spectrum(y4, 2)

# The mathematical phase is the shift compared to the cosine.
def print_magnitude_phase(t, y):
    yfft = np.fft.rfft(y) / n
    yfft[1:-1] *= 2.

    yfft10 = yfft[10]
    yfft10_magnitude = abs(yfft10)
    yfft10_phase = np.arctan2(yfft10.imag, yfft10.real)
    print 'Value = {0}, Magnitude = {1}, Phase = {2}'.format(yfft10,\
                                                             yfft10_magnitude,\
                                                             yfft10_phase)

    return yfft10

y3_10 = print_magnitude_phase(t, y3)
y4_10 = print_magnitude_phase(t, y4)
