import matplotlib.pyplot as plt
from scipy import signal

def plot_bode_diagram():
    w_n = 10.0
    zeta = 0.2
    num = [w_n ** 2]
    den = [1, 2 * zeta * w_n, w_n ** 2]

    sys = signal.TransferFunction(num, den)
    w, mag, phase = signal.bode(sys)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    plt.subplots_adjust(hspace=0.4)

    ax1.semilogx(w, mag, color='blue', linewidth=2)
    ax1.set_title('Διάγραμμα Bode - Μέτρο (Magnitude)', fontsize=14)
    ax1.set_ylabel('Μέτρο (dB)', fontsize=12)
    ax1.set_xlabel('Συχνότητα (rad/s)', fontsize=12)
    ax1.grid(True, which="both", ls="-", color='0.65')
    ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5)
    ax2.semilogx(w, phase, color='green', linewidth=2)
    ax2.set_title('Διάγραμμα Bode - Φάση (Phase)', fontsize=14)
    ax2.set_ylabel('Φάση (μοίρες)', fontsize=12)
    ax2.set_xlabel('Συχνότητα (rad/s)', fontsize=12)
    ax2.grid(True, which="both", ls="-", color='0.65')
    plt.show()

if __name__ == "__main__":
    plot_bode_diagram()
