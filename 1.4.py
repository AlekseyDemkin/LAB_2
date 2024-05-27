import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def Function1(t, a, b):
    return a * np.exp(-(b * t ** 2))


Function1 = np.vectorize(Function1)


def integrandL(t, a, b):
    return np.abs(Function1(t, a, b)) ** 2


def integrandR(w, a, b):
    return np.abs(fourier(w, a, b)) ** 2


def fourier(w, a, b):
    return (a * np.exp(-w ** 2 / (4 * b)) / np.sqrt(2 * b))


a = 10
b = 0.5
t_values = np.linspace(-10, 10, 1000)
w_values = np.linspace(-10, 10, 1000)
f_values = [Function1(t, a, b) for t in t_values]
L, errorL = quad(integrandL, -np.inf, np.inf, args=(a, b))
R, errorR = quad(integrandR, -np.inf, np.inf, args=(a, b))

print(f"Левая сторона условия Персеваля (L): {L}")
print(f"Правая сторона условия Персеваля (R): {R}")

plt.figure()
plt.plot(t_values, f_values, label='Function', color='blue')
plt.xlabel('t')
plt.ylabel('F(t)')
plt.title('Функция Гаусса')
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(w_values, fourier(w_values, a, b), label='Fourier image', color='red')
plt.xlabel('w')
plt.ylabel('c(w)')
plt.title('Фурье-образ функции Гаусса')
plt.grid(True)
plt.legend()

plt.show()
