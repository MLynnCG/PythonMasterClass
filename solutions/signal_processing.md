```python
import numpy as np
import matplotlib.pyplot as plt

# 1. Generate the signal
sampling_rate = 1000
duration = 1
t = np.linspace(0, duration, int(sampling_rate * duration))
frequency = 50
amplitude = 1
signal = amplitude * np.sin(2 * np.pi * frequency * t)

# 2. Perform FFT on the signal
fft_result = np.fft.fft(signal)

# 3. Generate the frequency array
frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)

# 4. Plot the signal waveform and the frequency spectrum
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Signal Waveform')

plt.subplot(1, 2, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')

plt.tight_layout()
plt.show()
```
