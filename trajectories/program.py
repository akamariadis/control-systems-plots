import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def pendulum_system(x, t, b, g, L):
    x1, x2 = x
    dxdt = [x2, -b*x2 - (g/L)*np.sin(x1)]
    return dxdt

b = 0.5
g = 9.81
L = 1.0
t = np.linspace(0, 20, 1000)

x1_range = np.linspace(-2, 2, 20)
x2_range = np.linspace(-2, 2, 20)
X1, X2 = np.meshgrid(x1_range, x2_range)
u, v = np.zeros(X1.shape), np.zeros(X2.shape)

for i in range(len(x1_range)):
    for j in range(len(x2_range)):
        dx = pendulum_system([X1[i,j], X2[i,j]], 0, b, g, L)
        u[i,j] = dx[0]
        v[i,j] = dx[1]

plt.figure(figsize=(10, 8))
plt.streamplot(X1, X2, u, v, color=(0.5, 0.5, 0.5, 0.3))
initial_conditions = [[1.5, 0], [-1.5, 1], [0.5, 2], [-0.5, -2]]
colors = ['r', 'g', 'b', 'orange']

for ic, color in zip(initial_conditions, colors):
    sol = odeint(pendulum_system, ic, t, args=(b, g, L))
    plt.plot(sol[:, 0], sol[:, 1], color=color, label=f'Αρχή: {ic}')
    plt.plot(ic[0], ic[1], 'o', color=color) # Σημείο εκκίνησης

plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title('Ευστάθεια Lyapunov: Τροχιές στο Επίπεδο Φάσης (Εκκρεμές)')
plt.xlabel('Θέση (x1)')
plt.ylabel('Ταχύτητα (x2)')
plt.legend()
plt.grid(True)
plt.show()
