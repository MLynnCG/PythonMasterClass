import numpy as np
import matplotlib.pyplot as plt

# Generate a signal
sampling_rate = 1000    # Sampling rate (samples per second)
duration = 2            # Duration of the signal in seconds
t = np.linspace(0, duration, int(sampling_rate * duration))   # Time array
frequency = 10          # Frequency of the signal in Hz
amplitude = 2           # Amplitude of the signal
signal = amplitude * np.sin(2 * np.pi * frequency * t)        # Signal waveform

# Perform FFT on the signal
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)  # Frequency array

# Plot the signal waveform
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Signal Waveform')

# Plot the frequency spectrum
plt.subplot(1, 2, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')

plt.tight_layout()
plt.show()
