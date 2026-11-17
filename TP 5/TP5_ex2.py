import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(0)

#===========Exercice 2===========
#=====question 1=====
def dice():
    die = rng.integers(1,7)
    return die

t = np.zeros(5, dtype=int)

#due to ex 2 demanding 100 000 simulations
# for i in range(5):
#     t[i] = dice()
#     print(f"throw {i+1} => {t[i]}")

#print(f"final score => {np.sum(t)}")

#=====question 2=====

n = 100000
S = np.zeros(n, dtype=int)

#here i was not sure if understood properly like do i do it 100 000 times instead of 5 or do 5 throws 100 000 times
for i in range(n):
    t2 = np.zeros(5 ,dtype=int)
    for j in range(5):
        t2[j] = dice()

    S[i] = np.sum(t2)

#print(f"final score => {S}")

#=====question 3=====

# bins = np.arange(4.5, 31, 1)

# plt.hist(S, bins=bins, color="lavender", edgecolor="plum")
# plt.xlabel("score from five throws")
# plt.ylabel("frequency")
# plt.title("scores from 100000 experiments")
# plt.show()

# counts = np.bincount(S)

# modes = np.where(counts == np.max(counts))[0]

# print(f"\nmode: {modes}")
# print(f"highest frequency: {np.max(counts)}")

#=====question 4=====
sc = 0

for i in range(20):
    t4 = dice()
    sc += t4

    if sc >= 20:
        break

# print(f"number of throws: {i+1}")
# print(f"final score: {sc}")
#=====question 5=====

sc5 = 0
t5 = 0

while sc5 < 20:
    x = dice()
    sc5 += x
    t5 += 1

# print(f"number of throws: {t5}")
# print(f"final score: {sc5}")

#=====question 6=====

def scoremin(m):
    sc = 0
    t6 = 0

    if not isinstance(m, (int, np.integer)) or m <= 0:
        raise ValueError("m gotta be a positive integer")

    while sc < m:
        sc += dice()
        t6 += 1

    return t6

#print(f"throws to reach at least 20: {scoremin(20)}")

#=====question 7=====

n7 = 1000
I = np.zeros(n7, dtype=int)

for i in range(n7):
    I[i] = scoremin(20)

hf = np.bincount(I)
md7 = np.where(hf == np.max(hf))[0]

# print(f"numbers of throws: {I}")
# print(f"mode => {md7}")
# print(f"highest frequency => {np.max(hf)}")

#=====bonus=====
def diceP(p):
    if p < 0 or p > 1:
        raise ValueError("p doesnt satistfy requirements")

    f = np.arange(1, 7)
    proba = [(1-p)/5] * 5 + [p]
    d = rng.choice(f, p=proba)

    return d

def scoreminP(m, p):
    if not isinstance(m, (int, np.integer)) or m <= 0:
        raise ValueError("m must be a positive integer")

    sc = 0
    ts = 0

    while sc < m:
        sc += diceP(p)
        ts += 1

    return ts

p8 = 1/6
n8 = 1000
selectp = None
prevp = None

while p8 <= 1:
    I8 = np.zeros(n8, dtype=int)

    for i in range(n8):
        I8[i] = scoreminP(20, p8)

    counts8 = np.bincount(I8)
    md8 = np.where(counts8 == np.max(counts8))[0]

    print(f"p = {p8:.4f}, mode = {md8}")

    if 4 in md8:
        selectp = p8
        break

    prevp = p8
    p8 += 0.1

if selectp is not None:
    print(f"selected probability => {selectp}")
else:
    print("No 4")

#check with 10,000 experiments
n8 = 10000

if selectp is not None:
    for p8 in [prevp, selectp]:
        if p8 is None:
            continue

        I8 = np.zeros(n8, dtype=int)

        for i in range(n8):
            I8[i] = scoreminP(20, p8)

        counts8 = np.bincount(I8)
        md8 = np.where(counts8 == np.max(counts8))[0]

        print(f"check: p = {p8} and mode = {md8}")