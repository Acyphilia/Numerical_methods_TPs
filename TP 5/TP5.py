import numpy as np
import matplotlib.pyplot as plt

#===========Exercice 1===========

rng = np.random.default_rng(0)
p = 0.05

#=====question 1=====

u = rng.uniform()

if u < p :
    s = 1
else:
    s = 0

s1 = int(u<p)

#print(f"with if-else statement: {s}", f"\nwithout the if-else statement: {s1}")
#print("are they the same:", s == s1)

#=====question 2=====
working_days = 70
array_s = np.zeros(70, dtype=int)
for i in range(working_days):
    u = rng.uniform()
    if u < p:
        array_s[i] = 1
    else:
        array_s[i] = 0

N_inspections = np.sum(array_s)
#print(f"daily outcomes: {array_s}", f"\nnumber of inspections:{N_inspections}")

#=====question 3=====

U = rng.uniform(size=70)
array_s1 = (U<p).astype(int)

array_s2 = np.zeros(70, dtype=int)
for i in range(70):
    if U[i] < p:
        array_s2[i] = 1
    else:
        array_s2[i] = 0
    
#print(f"daily outcomes: {array_s1}", f"\nnumber of inspections:{np.sum(array_s1)}")
#print(f"do the non for loop and for loop arrays contain the same value => {np.array_equal(array_s2,array_s1)}")

#=====question 4=====
u = rng.uniform()
days = 1

while u >= p:
        u = rng.uniform()
        days += 1

#print(f"days until first inspection: {days}") 

#=====question 5=====
fine = 100
working_days_month = 21

def daysUntilChecked(p):
    if p > 0 and p <= 1:
        u = rng.uniform()
        days = 1

        while u >= p:
            u = rng.uniform()
            days += 1

        return days
    
    else:
        raise ValueError("p must satisfy 0 < p <= 1")           

d = daysUntilChecked(0.05)
c = 100 * 21 / d

#print(f"days until first inspection: {d}")
#print(f"single-cycle monthly rate: {c}CHF")

#=====question 6=====

p6 = 0.05
m = 10**4

wait_time = np.zeros(m, dtype=int)

for i in range(m):
    wait_time[i] = daysUntilChecked(p6)

D = np.mean(wait_time)
C6 = 100 * 21 / D

#print(f"average days until inspection: {D}")
#print(f"estimated monthly cost: {C6}CHF")

#=====question 7=====

p7 = 0.05
m7 = 10**4
p0 = None

while p7 > 0:
    wait_time = np.zeros(m7, dtype=int)

    for i in range(m7):
        wait_time[i] = daysUntilChecked(p7)

    D = np.mean(wait_time)
    C7 = 100 * 21 / D

    print(f"p = {p7}")
    print(f"average days = {D}")
    print(f"Cost = {C7}CHF")

    if C7 < 45:
        p0 = p7
        break

    p7 = round(p7 - 0.002, 3)

if p0 is not None:
    expected_inspections = 70 * p0

    print(f"\nselected probability: {p0}")
    print(f"expected inspections in 70 days: {expected_inspections}")
else:
    print("no positive tested probability")
