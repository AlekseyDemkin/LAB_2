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

# Найти индексы трех самых высоких значений в модуле Фурье-образа
top_indices = np.argsort(np.abs(fourier))[-3:]

plt.figure()
plt.plot(freq_values, np.abs(fourier), color='blue')
plt.xlabel('Частота (Гц)')
plt.ylabel('|f(ν)|')
plt.title('График модуля Фурье-образа')

# Вывести тройку самых высоких частот
for index in top_indices:
    frequency = freq_values[index]
    magnitude = np.abs(fourier[index])
    plt.annotate(f'({frequency:.2f} Гц, {magnitude:.2f})', (frequency, magnitude), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()
