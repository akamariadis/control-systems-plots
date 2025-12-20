import control as ct
import matplotlib.pyplot as plt
import numpy as np

num = [1]
den = [1, 6, 8, 0]
sys = ct.TransferFunction(num, den)

print("Η Συνάρτηση Μεταφοράς Ανοικτού Βρόχου είναι:")
print(sys)

plt.figure(figsize=(10, 6))
rlist, klist = ct.root_locus(sys, grid=False) 
plt.title('Γεωμετρικός Τόπος Ριζών (Root Locus)\n Σύστημα: $G(s) = \\frac{1}{s(s+2)(s+4)}$')
plt.xlabel('Πραγματικός Άξονας (Real Axis - $\sigma$)')
plt.ylabel('Φανταστικός Άξονας (Imaginary Axis - $j\omega$)')
plt.axvline(0, color='black', lw=1)
plt.axhline(0, color='black', lw=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.plot(np.real(sys.pole()), np.imag(sys.pole()), 'rx', markersize=10, label='Πόλοι Ανοικτού Βρόχου (Open Loop Poles)')
plt.legend()
plt.show()
