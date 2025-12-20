import numpy as np
import control as ct
import matplotlib.pyplot as plt

num = [1]
den = [1, 6, 8, 0]
G_s = ct.TransferFunction(num, den)

gains = [2, 10, 35]
labels = ['K=2 (Αργό)', 'K=10 (Ισορροπημένο)', 'K=35 (Ταλαντώσεις)']
colors = ['green', 'blue', 'red']

plt.figure(figsize=(10, 6))

for K, label, color in zip(gains, labels, colors):
    T_s = ct.feedback(K * G_s, 1)
    t, y = ct.step_response(T_s, T=np.linspace(0, 15, 1000))
    plt.plot(t, y, label=label, color=color, linewidth=2)

plt.title('Επίδραση του Κέρδους (K) στην Απόκριση του Συστήματος')
plt.xlabel('Χρόνος (sec)')
plt.ylabel('Έξοδος Συστήματος (Επιθυμητή τιμή = 1)')
plt.axhline(1, color='black', linestyle='--', label='Στόχος (Set point)')
plt.grid(True, alpha=0.5)
plt.legend()
plt.show()
