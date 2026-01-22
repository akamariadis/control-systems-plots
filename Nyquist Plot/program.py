import numpy as np
import matplotlib.pyplot as plt
import control as ct

def plot_nyquist_criterion():
    numerator = [50]
    denominator = [1, 6, 11, 6]
    sys = ct.TransferFunction(numerator, denominator)

    print("Συνάρτηση Μεταφοράς:")
    print(sys)

    gm, pm, wg, wp = ct.margin(sys)

    print(f"\nΑνάλυση Ευστάθειας:")
    print(f"Περιθώριο Κέρδους (GM): {gm:.2f} (σε απόλυτη τιμή)")
    print(f"Περιθώριο Φάσης (PM): {pm:.2f} μοίρες")

    if gm > 1:
        print("-> Το σύστημα Κλειστού Βρόχου είναι ΕΥΣΤΑΘΕΣ.")
    else:

        print("-> Το σύστημα Κλειστού Βρόχου είναι ΑΣΤΑΘΕΣ.")

    plt.figure(figsize=(10, 8))
    ct.nyquist_plot(sys, arrows=True)
    plt.plot(-1, 0, 'rx', markersize=10, markeredgewidth=3, label='Κρίσιμο Σημείο (-1+0j)')
    theta = np.linspace(0, 2 * np.pi, 100)
    plt.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.3, label='Μοναδιαίος Κύκλος')
    plt.title(f'Διάγραμμα Nyquist\n$G(s) = 50 / (s^3 + 6s^2 + 11s + 6)$')
    plt.xlabel('Real Axis')
    plt.ylabel('Imaginary Axis')
    plt.grid(True, which='both', linestyle=':', alpha=0.6)
    plt.legend()
    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)
    plt.show()

if __name__ == "__main__":
    plot_nyquist_criterion()
