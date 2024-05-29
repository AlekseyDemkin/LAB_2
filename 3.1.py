import numpy as np
import matplotlib.pyplot as plt
import librosa

audio_path = 'Аккорд (23).mp3'
data, rate = librosa.load(audio_path)

max_freq = rate / 2
freq_step = 1
freq_values = np.arange(0, max_freq, freq_step)
fourier = np.zeros(len(freq_values), dtype=complex)

for v in range(len(freq_values)):
    fourier[v] = np.trapz(data * np.exp(-1j * 2 * np.pi * freq_values[v] * np.arange(len(data)) / rate))


top_indices = np.argsort(np.abs(fourier))[-3:]

top_frequencies = freq_values[top_indices]
print("Три самых высоких частоты:", top_frequencies)
plt.figure()
plt.plot(freq_values, np.abs(fourier), color='blue')
plt.xlabel('Частота (Гц)')
plt.ylabel('|f(ν)|')
plt.title('График модуля Фурье-образа')
plt.show()
