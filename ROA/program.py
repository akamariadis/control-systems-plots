import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def system(x, t):
    x1, x2 = x
    dx1dt = x2
    dx2dt = -x1 + x1**3 - x2
    return [dx1dt, dx2dt]

x1_range = np.linspace(-2, 2, 40)
x2_range = np.linspace(-2, 2, 40)
T = np.linspace(0, 20, 200)

plt.figure(figsize=(10, 8))

for x1_init in x1_range:
    for x2_init in x2_range:
        sol = odeint(system, [x1_init, x2_init], T)
        final_state = sol[-1]
        if np.linalg.norm(final_state) < 0.1:
            plt.plot(x1_init, x2_init, 'go', markersize=2, alpha=0.3)
        else:
            plt.plot(x1_init, x2_init, 'ro', markersize=2, alpha=0.3)

X1, X2 = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
U, V = X1*0, X2*0
for i in range(len(X1)):
    for j in range(len(X1[0])):
        dx = system([X1[i,j], X2[i,j]], 0)
        U[i,j] = dx[0]
        V[i,j] = dx[1]

plt.streamplot(X1, X2, U, V, color='k', linewidth=0.5)
plt.title('Region of Attraction (Green) for Equilibrium (0,0)')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.grid(True)
plt.show()
