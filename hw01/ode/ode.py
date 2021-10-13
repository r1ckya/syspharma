import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint


def ode_system(x, t):
    k1 = 0.5
    k2 = 1
    k_plus = 1
    k_minus = 1
    k3 = 0.5

    S1, S2, P = x

    v = k_plus * S1 * S2 - k_minus * P * P
    dS1 = k1 - v
    dS2 = k2 - v
    dP = 2 * v - k3 * P

    return [dS1, dS2, dP]


def main():
    x0 = [0, 0, 0]
    t = np.linspace(0, 20, 10000)
    x = odeint(ode_system, x0, t)

    S1 = x[..., 0]
    S2 = x[..., 1]
    P = x[..., 2]

    plt.semilogy(t, S1, label="S1")
    plt.semilogy(t, S2, label="S2")
    plt.semilogy(t, P, label="P")
    plt.legend()
    plt.savefig("reagents.png")
    plt.show()


if __name__ == "__main__":
    main()
