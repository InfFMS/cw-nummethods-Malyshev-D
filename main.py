import numpy as np
import matplotlib.pyplot as plt
#
#1
def f(T, V):
    P = (8.314*T/(V-3.19*10**(-5))) - 0.1382/V**2
    return P

t = np.array([133.15, 143.15, 153.15, 163.15, 173.15])
x = np.linspace(4.19*10**(-5), 10**(-3), 10000)
fig, axs = plt.subplots(1, 6, figsize=(14, 4))  # 1 ряд, 2 столбца

for i in range(5):
    y = f(t[i], x)
    axs[i].plot(x, y, color="blue")
    axs[i].set_xlabel("V")
    axs[i].set_ylabel("P")
for i in range(5):
    axs[i].plot(x, f(t[3], x), color='red')
#
#
#4
def f1(T, V):
    P1 = f(T, V) - 3664186.998
    return P1
axs[5].plot(x, f1(t[1], x) , color='green')
axs[5].axhline(0, color='red', lw=0.5)
a = 0.00005
b = 0.00007

while b - a > 2* 10**-7:
    c = (a+b)/2
    if f(t[1],a)*f(t[1],c) < 0:
        b = c
    else: a = c
print(c, f1(t[1],c))






plt.tight_layout()
plt.show()