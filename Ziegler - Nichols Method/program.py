import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def system_dynamics(y, t, u, Kp):  
    x1, x2, x3 = y    
    dx1dt = x2
    dx2dt = x3
    dx3dt = u - 3*x3 - 3*x2 - x1
    return [dx1dt, dx2dt, dx3dt]

#CLOSED LOOP ZIEGLER - NICHOLS
def simulate_closed_loop():
    t = np.linspace(0, 20, 1000)
    y0 = [0, 0, 0]
    Setpoint = 1.0
    Kcr = 8.0 
    
    def closed_loop_ode(y, t):
        e = Setpoint - y[0]
        u = Kcr * e
        return system_dynamics(y, t, u, Kcr)

    sol = odeint(closed_loop_ode, y0, t)
    y_out = sol[:, 0]

    plt.figure(figsize=(10, 6))
    plt.plot(t, y_out, 'b', label=f'Output y(t) with Kp = Kcr = {Kcr}')
    plt.plot(t, [Setpoint]*len(t), 'r--', label='Setpoint')
    plt.title(f'Μέθοδος Κλειστού Βρόχου: Αμετάβλητες Ταλαντώσεις (Kcr={Kcr})')
    plt.xlabel('Χρόνος (sec)')
    plt.ylabel('Έξοδος')
    plt.grid(True)
    
    peaks = []
  
    for i in range(1, len(y_out)-1):
        if y_out[i-1] < y_out[i] and y_out[i] > y_out[i+1]:
            peaks.append(t[i])
    
    if len(peaks) >= 2:
        Pcr = peaks[1] - peaks[0]
        plt.annotate(f'Pcr ≈ {Pcr:.2f} sec', 
                     xy=(peaks[0], y_out[int(peaks[0]*50)]), 
                     xytext=(peaks[0]+1, y_out[int(peaks[0]*50)]+0.2),
                     arrowprops=dict(facecolor='black', shrink=0.05))
        plt.hlines(y=y_out[int(peaks[0]*50)], xmin=peaks[0], xmax=peaks[1], colors='g', linestyles='--')

    plt.legend()
    plt.show()

#OPEN LOOP ZIEGLER - NICHOLS
def simulate_open_loop():
    t = np.linspace(0, 20, 1000)
    y0 = [0, 0, 0]
    u_step = 1.0
    
    def open_loop_ode(y, t):
        return system_dynamics(y, t, u_step, 0)

    sol = odeint(open_loop_ode, y0, t)
    y_out = sol[:, 0]
    K_proc = (y_out[-1] - y_out[0]) / u_step
    dydt = np.gradient(y_out, t)
    max_dydt_idx = np.argmax(dydt)
    slope = dydt[max_dydt_idx]
    t_inflection = t[max_dydt_idx]
    y_inflection = y_out[max_dydt_idx]
    L = t_inflection - (y_inflection / slope)
    T = K_proc / slope
    t_tangent = np.linspace(L, L+T, 100)
    y_tangent = slope * (t_tangent - L)

    plt.figure(figsize=(10, 6))
    plt.plot(t, y_out, 'b', label='Process Variable (PV)')
    plt.plot(t_tangent, y_tangent, 'r--', label='Εφαπτομένη (Tangent)')
    plt.hlines(y_out[-1], 0, 20, colors='gray', linestyles='dotted', label='Τελική Τιμή')
    plt.annotate(f'L = {L:.2f}s', xy=(L, 0), xytext=(L+1, 0.1),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))
    plt.hlines(y=y_out[-1], xmin=L, xmax=L+T, colors='green', alpha=0.3)
    plt.vlines(x=L+T, ymin=0, ymax=y_out[-1], colors='green', linestyles='dashed')
    plt.annotate(f'T = {T:.2f}s', xy=(L + T/2, y_out[-1]), xytext=(L + T/2, y_out[-1]-0.2),
                 ha='center', color='green', fontweight='bold')
    plt.title(f'Μέθοδος Ανοιχτού Βρόχου: Υπολογισμός L και T\n(K={K_proc:.1f}, L={L:.2f}s, T={T:.2f}s)')
    plt.xlabel('Χρόνος (sec)')
    plt.ylabel('Έξοδος')
    plt.ylim(-0.1, 1.2)
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print("\n--- Αποτελέσματα Ανοιχτού Βρόχου ---")
    print(f"Κέρδος Διεργασίας (K): {K_proc:.2f}")
    print(f"Νεκρός Χρόνος (L): {L:.2f} sec")
    print(f"Χρονική Σταθερά (T): {T:.2f} sec")
    print("\nΠροτεινόμενες Ρυθμίσεις PID (Ziegler-Nichols Open Loop):")
    Kp_pid = 1.2 * (T / (K_proc * L))
    Ti_pid = 2 * L
    Td_pid = 0.5 * L
    print(f"Kp = {Kp_pid:.3f}")
    print(f"Ti = {Ti_pid:.3f} sec")
    print(f"Td = {Td_pid:.3f} sec")

if __name__ == "__main__":
    simulate_closed_loop()
    simulate_open_loop()
