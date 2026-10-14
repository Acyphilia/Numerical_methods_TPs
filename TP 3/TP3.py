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
        count += 1

#print(count)

##=====Question 4=====
#note break on first entry below 0.1 dont run after
#keep the verif false so if the first entry isnt <0.1 
verif = False

for i in range(len(U)):
    if U[i] < 0.1:
        print("question 4:\n","index: ", i, "\nvalue: ", U[i], "\nnumber of entries examined: ", i+1, "\n\n")

        verif = True
        break

if verif == False :
    print("No value below 0.1 was found")

##=====Question 5=====
j = 1
while u >= 0.1:
    u = rng.uniform()
    j += 1

#print("successful value: ", u, "\ntotal number of draws: ", j)

##=====Question 6=====
ind = 0
while U[ind] >= 0.1:
    ind += 1

#print("index:", ind, "\nvalue:", U[ind],"\number of entries examined:", ind + 1)

##=====Question 7=====
t = 0.00001
ix = 0
while ix < len(U) and U[ix] >= t:
    ix += 1

if ix < len(U):
    print("index: ", ix, "value: ", U[ix],"number of entries examined: ", ix + 1)

else:
    print("No matching value found\nNumber of entries examined: ", len(U), "\n")

##==========EXERCICE 3===========
print("all questions covered in exercice 3")
##=====Question 1=====
def first_below(U, t):
    index = 0
    while index < len(U) and U[index] >= t:
        index += 1 

    if index < len(U):
        return (index, U[index], True)
    else:
        return (None, None, False)

##=====Question 2 & 3=====
#print(first_below(np.array([0.05, 0.4, 0.8]), 0.1))
#print(first_below(np.array([0.4, 0.05, 0.8]), 0.1))
#print(first_below(np.array([0.4, 0.8, 0.05]), 0.1))
#print(first_below(np.array([0.4, 0.8, 0.2]), 0.1))
#print(first_below(np.array([0.1, 0.4, 0.05]), 0.1))
#print(first_below(np.array([]), 0.1))

