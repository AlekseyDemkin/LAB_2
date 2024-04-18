import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad


def Function1(t, a, b):
    if abs(t) <= b:
        return a - abs(a * t / b)
    if abs(t) > b:
        return 0


Function1 = np.vectorize(Function1)


def integrandL(t, a, b):
    return np.abs(Function1(t, a, b)) ** 2


def integrandR(w, a,b):
    return np.abs(fourier(w, a,b)) ** 2


def fourier(w, a, b):
    return (1/math.sqrt(2*np.pi))*a*(2-2*np.cos(b*w))/(b*w**2)


a = 7
b = 7

t_values = np.linspace(-10, 10, 1000)
w_values = np.linspace(-10, 10, 1000)
f_values = [Function1(t, a, b) for t in t_values]
L, errorL = quad(integrandL, -np.inf, np.inf, args=(a, b))
R, errorR = quad(integrandR, -np.inf, np.inf, args=(a, b))
print(f"Левая сторона условия Персеваля (L): {L}")
print(f"Правая сторона условия Персеваля (R): {R}")
#plt.plot(t_values, f_values, label='Function', color='blue')
plt.plot(w_values, fourier(w_values, a, b), label='Fourier image', color='red')
plt.xlabel('w')
plt.ylabel('c(w)')
plt.title('Треугольная функция')
plt.title('Фурье образ треугольной функции')
plt.legend()
plt.grid(True)
plt.show()
