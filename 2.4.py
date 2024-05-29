import numpy as np
import matplotlib.pyplot as plt



def Function1(t, a, b, c):
    return a * np.exp(-(b * (t + c) ** 2))


Function1 = np.vectorize(Function1)


def fourier(w, a, b, c):
    return (a * np.exp(1j * c * w) * np.exp(-w ** 2 / (4 * b)) / np.sqrt(2 * b))


a = 3
b = 1
c = 20
t_values = np.linspace(-10, 10, 1000)
w_values = np.linspace(-10, 10, 1000)
f_values = [Function1(t, a, b, c) for t in t_values]

plt.figure()
plt.plot(t_values, f_values, label='Function', color='blue')
plt.xlabel('t')
plt.ylabel('F(t)')
plt.title('Функция Гаусса')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(w_values, np.real(fourier(w_values, a, b, c)), label='Real', color='red')
plt.xlabel('w')
plt.ylabel('c(w)')
plt.title('Вещественная часть')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(w_values, np.imag(fourier(w_values, a, b, c)), label='Image', color='green')
plt.xlabel('w')
plt.ylabel('c(w)')
plt.title('Мнимая часть')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(w_values, np.abs(fourier(w_values, a, b, c)), label='abs', color='purple')
plt.xlabel('w')
plt.ylabel('c(w)')
plt.title('Модуль Фурье-образа')
plt.grid(True)
plt.legend()
plt.show()
