import numpy as np
rng = np.random.default_rng(0)
x = np.ceil(9 * rng.uniform(size=15)).astype(int)
p = np.flatnonzero(x > 5)

##==========EXERCICE 1===========
#=====Question 1=====

#for x = np.ceil(9 * rng.uniform(size=15)).astype(int), we generate 15 random numbers from 0 to 1 then 
#multiply by 9, with np.ciel we round the number and turn it to an int

#help(np.flatnonzero)
#p = np.flatnonzero(x > 5), return the indices where the condition is true

##=====Question 2=====
p2 = np.array([], dtype=int)
for i in range(len(x)):
    if x[i] > 5:
        p2 = np.append(p2, i)

#print(p2)
#print(np.array_equal(p2, p))

##=====Question 3=====
def f(x, t):
    f = np.empty((0,2), dtype=x.dtype)
    for i in range(len(x)):
        if x[i] > t:
            f = np.append(f, [[i, x[i]]], axis = 0)

    return f

#print(f(x,5))
#print(f(x,np.max(x)+1))

##==========EXERCICE 2===========
#=====Question 1=====
u = rng.uniform()
#print(u)
#print(u<0.1)

#=====Question 2=====
U = rng.uniform(size=50)
#print(U)

#=====Question 3=====
count = 0
for i in range(len(U)):
    if U[i] < 0.1:
        c = c + 1

#print(count)

##=====Question 4=====

