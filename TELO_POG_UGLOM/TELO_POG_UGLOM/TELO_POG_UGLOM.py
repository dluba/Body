import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 10
alpha = 45
t = 0
dt = 0.005
m = 1
Q = input("Сопротивление воздуха есть? - ")

x = []
y = []

if Q == "Нет":
    while t <= 2: # без сопротивления
        t += dt
        x_value = v0 * np.cos(alpha) * t
        y_value = v0 * np.sin(alpha) * t - (g * t ** 2) / 2
        x.append(x_value)
        y.append(y_value)
        print(x_value, y_value)
        if y_value < 0:
            break

if Q == "Да":
    R = input("Введите значение сопротивления воздуха: ")
    while t <= 2:
        t += dt
        exp = np.exp(- float(R) * t / m)
        x_value = (v0 * np.cos(alpha) * m / float(R)) * (1 - exp)
        y0 = (m * g + v0 * np.sin(alpha) * float(R)) * m
        y_value = (- (y0 * exp) / (float(R) ** 2)) - (g * m * t / float(R)) + y0 / float(R) ** 2
        x.append(x_value)
        y.append(y_value)
        print(x_value, y_value)
        if y_value < 0:
            break

plt.title('Полёт тела под углом к горизонту')
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y)

plt.show()
