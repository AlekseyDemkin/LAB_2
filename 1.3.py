import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad

def Function1(t, a, b):
    return a * np.sinc(b * t)

Function1 = np.vectorize(Function1)

def integrandL(t, a, b):
    return np.abs(Function1(t, a, b)) ** 2

def integrandR(w, a, b):
    return np.abs(fourier(w, a, b)) ** 2

def fourier(w, a, b):
    for i in w:
        if abs(i) > np.pi * b:
            return (a / abs(b)) * 0
        elif abs(i) == np.pi * b:
            return (a / abs(b)) * 0.5
        else:
            return (a / abs(b)) * 1

a = 5
b = 5
w_values = np.linspace(-10, 10, 1000)
L, errorL = quad(integrandL, -np.inf, np.inf, args=(a, b))
R, errorR = quad(integrandR, -np.inf, np.inf, args=(a, b))

print(f"Левая сторона условия Персеваля (L): {L}")
print(f"Правая сторона условия Персеваля (R): {R}")
# plt.plot(t_values, f_values, label='Function', color='blue')
plt.plot(w_values, fourier(w_values, a, b), label='Fourier image', color='red')
plt.xlabel('w')
plt.ylabel('c(w)')
plt.title('Треугольная функция')
plt.title('Фурье образ треугольной функции')
plt.legend()
plt.grid(True)
plt.show()
