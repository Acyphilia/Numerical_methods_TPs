import numpy as np
import matplotlib.pyplot as plt

#===========Exercice 1===========
#=====question 1=====
def p(x):
    p = (x - 2)**5
    return p

def f(x):
    f = x**5 - 10*x**4 + 40*x**3 - 80*x**2 + 80*x - 32
    return f

x = np.linspace(1.998, 2.002, 41)
px = p(x)
fx = f(x)
#print(f"f(x) = {fx}")
#print(f"\np(x) = {px}")

#=====question 2=====
plt.figure()
plt.plot(x, px, color="blue", label="p(x) = (x - 2)^5")
plt.plot(x, fx, color="pink", marker="o", label="f(x) expanded form")
plt.xlabel("x")
plt.ylabel("function value")
plt.title("comparison of p(x) and f(x)")
plt.legend()
plt.grid()
plt.show()

#even tho both expressions represent the same polynomial their numerical results differ
#the factored form p(x) produces a smooth curve, while the expanded form f(x) fluctuates due to rounding errors and cancellation between large terms.

#=====question 3=====   
x3 = np.linspace(1000.998, 1001.002, 41)

p3 = p(x3)
f3 = f(x3)

diff = f3 - p3

plt.figure()
plt.plot(x3, diff, color="purple", marker="o",
         label="f(x) - p(x)")

plt.axhline(0, color="black", linestyle="--")
plt.xlabel("x")
plt.ylabel("f(x) - p(x)")
plt.title("difference between the two expressions")
plt.legend()
plt.grid()
plt.show()

#===========Exercice 2===========
U = np.zeros(31, dtype=float)
S = np.zeros(31, dtype=float)
R = np.zeros(31, dtype=float)
U[0] = 1
S[0] = 0

for n in range(1, 31):
    U[n] = (1/4) * U[n - 1]
    S[n] = S[n - 1] + U[n]
    R[n] = (1 - 3*S[n]) / U[n]

nv = np.arange(1, 31)

plt.figure()
plt.plot(nv, R[1:], marker="o", label="R_n")
plt.plot(nv, S[1:], label="S_n")
plt.plot(nv, U[1:], label="u_n")
plt.xlabel("n")
plt.ylabel("value")
plt.title("behaviour of the three sequences")
plt.legend()
plt.grid()
plt.show()
