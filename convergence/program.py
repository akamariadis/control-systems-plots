import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-2, 2, 20)
x2 = np.linspace(-2, 2, 20)
X1, X2 = np.meshgrid(x1, x2)

def get_dynamics(A, X1, X2):
    u = A[0,0]*X1 + A[0,1]*X2
    v = A[1,0]*X1 + A[1,1]*X2
    return u, v
cases = {
    "1. Σπειροειδής Σύγκλιση (Stable Focus)": np.array([[-0.5, 1], [-1, -0.5]]),
    "2. Άμεση Σύγκλιση (Stable Node)": np.array([[-1, 0], [0, -2]]),
    "3. Συνεχής Περιστροφή (Center)": np.array([[0, 1], [-1, 0]]),
    "4. Απομάκρυνση (Unstable Focus)": np.array([[0.5, 1], [-1, 0.5]])
}

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.ravel()

for i, (title, A) in enumerate(cases.items()):
    U, V = get_dynamics(A, X1, X2)
    axs[i].streamplot(X1, X2, U, V, color='blue', linewidth=1, density=1.2)
    axs[i].axhline(0, color='black', lw=1)
    axs[i].axvline(0, color='black', lw=1)
    axs[i].set_title(title)
    axs[i].set_xlabel('$x_1$')
    axs[i].set_ylabel('$x_2$')
    axs[i].grid(True, linestyle='--', alpha=0.6)
  
plt.tight_layout()
plt.show()
