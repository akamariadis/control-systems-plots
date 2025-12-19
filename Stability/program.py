import numpy as np
import matplotlib.pyplot as plt
import control as ct

sys_stable = ct.TransferFunction([1], [1, 2, 2])
sys_unstable = ct.TransferFunction([1], [1, -0.5, 2])

t = np.linspace(0, 20, 1000)

t_s, y_s = ct.step_response(sys_stable, t)
t_u, y_u = ct.step_response(sys_unstable, t)

t_si, y_si = ct.impulse_response(sys_stable, t)
t_ui, y_ui = ct.impulse_response(sys_unstable, t)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].plot(t_s, y_s, 'b')
axes[0, 0].set_title('Ευσταθές Σύστημα: Βηματική Απόκριση (BIBO)')
axes[0, 0].grid(True)

axes[0, 1].plot(t_u, y_u, 'r')
axes[0, 1].set_title('Ασταθές Σύστημα: Βηματική Απόκριση (BIBO)')
axes[0, 1].grid(True)

axes[1, 0].plot(t_si, y_si, 'g')
axes[1, 0].set_title('Ευσταθές Σύστημα: Απόκριση Κρούσης (Lyapunov)')
axes[1, 0].grid(True)

axes[1, 1].plot(t_ui, y_ui, 'orange')
axes[1, 1].set_title('Ασταθές Σύστημα: Απόκριση Κρούσης (Lyapunov)')
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

print(f"Πόλοι Ευσταθούς Συστήματος: {sys_stable.poles()}")
print(f"Πόλοι Ασταθούς Συστήματος: {sys_unstable.poles()}")
