import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad


def Function1(t, a, b):
    if abs(t) <= b:
        return a
    if abs(t) > b:
        return 0


Function1 = np.vectorize(Function1)


def integrandL(t, a, b):
    return np.abs(Function1(t, a, b)) ** 2


def integrandR(w, a):
    return np.abs(fourier(w, a)) ** 2


def fourier(w, a):
    if w == 0:
        return 0
    else:
        return (2 * a * np.sin(b * w)) / (math.sqrt(2 * np.pi) * w)



a = 7
b = 7

t_values = np.linspace(-10, 10, 1000)
w_values = np.linspace(-10, 10, 1000)
f_values = [Function1(t, a, b) for t in t_values]
L, errorL = quad(integrandL, -np.inf, np.inf, args=(a, b))
R, errorR = quad(integrandR, -np.inf, np.inf, args=(a))
print(f"Левая сторона условия Персеваля (L): {math.sqrt(L)}")
print(f"Правая сторона условия Персеваля (R): {math.sqrt(R)}")
# plt.plot(t_values, f_values, label='Function', color='blue')
plt.plot(w_values, fourier(w_values, a), label='Fourier image', color='red')
plt.xlabel('w')
plt.ylabel('c(w)')
# plt.title('Прямоугольная функция')
plt.title('Фурье образ прямоугольная функция')
plt.legend()
plt.grid(True)
plt.show()
