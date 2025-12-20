import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

wn = 5.0
zetas = [0.2, 1.0, 3.0]
labels = ['Υποκρίσιμη (ζ=0.2)', 'Κρίσιμη (ζ=1.0)', 'Υπερκρίσιμη (ζ=3.0)']
colors = ['red', 'green', 'blue']

t = np.linspace(0, 4, 1000)

plt.figure(figsize=(10, 6))

for zeta, label, color in zip(zetas, labels, colors):
    num = [wn ** 2]  # Αριθμητής
    den = [1, 2 * zeta * wn, wn ** 2]
    system = signal.TransferFunction(num, den)
    t_out, y_out = signal.step(system, T=t)
    plt.plot(t_out, y_out, label=label, color=color, linewidth=2)

plt.axhline(y=1.0, color='black', linestyle='--', alpha=0.6, label='Στόχος (Setpoint)')
plt.title(f'Βηματική Απόκριση Συστημάτων 2ης Τάξης (ωn={wn} rad/s)', fontsize=14)
plt.xlabel('Χρόνος (s)', fontsize=12)
plt.ylabel('Πλάτος (y)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
