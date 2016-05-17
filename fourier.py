import numpy as np
from scipy import signal
import matplotlib.pyplot as pl
pl.ion()

n = 100000
t = np.linspace(0., 20*np.pi, n)

# We introduce three series:
# y1 is a superposition of two waves
# y2 is y1 plus a linear trend
# y2d is the detrended version of y2

y1 = np.sin(t) + np.sin(4.*t)
y2 = np.sin(t) + np.sin(4.*t) + 3./(20.*np.pi)*t
y2d = signal.detrend(y2)

def plot_spectrum(y, nfig):
    # An FFT of real data.
    yfft = np.fft.rfft(y)

    # Division by the number of samples, as the FFT
    # multiplies the values by that number.
    yfft /= n

    # Correct the data for the absense of the complex conjugate.
    yfft[1:-1] *= 2.
   
    # Plot the series and its spectrum.
    pl.figure(nfig)
    pl.subplot(211)
    pl.plot(t, y)
    pl.subplot(212)
    pl.semilogx(abs(yfft))

plot_spectrum(y1 , 1)
plot_spectrum(y2 , 1)
plot_spectrum(y2d, 1)

# Calculate the magnitude and phase of these two series.
y3 = np.sin(t)
y4 = 0.5*np.cos(t)

plot_spectrum(y3, 2)
plot_spectrum(y4, 2)

def print_magnitude_phase(t, y):
    yfft = np.fft.rfft(y) / n
    yfft[1:-1] *= 2.

    yfft10 = yfft[10]

    # The magnitude is (Re(yfft)**2 + Im(yfft)**2)**(1/2)
    yfft10_magnitude = abs(yfft10)

    # The mathematical phase is the shift compared to the cosine.
    yfft10_phase = np.arctan2(yfft10.imag, yfft10.real)
    print 'Value = {0}, Magnitude = {1}, Phase = {2}'.format(yfft10,\
                                                             yfft10_magnitude,\
                                                             yfft10_phase)

    return yfft10, yfft10_magnitude, yfft10_phase

y3_10, y3_10_magnitude, y3_10_phase = print_magnitude_phase(t, y3)
y4_10, y4_10_magnitude, y4_10_phase = print_magnitude_phase(t, y4)
