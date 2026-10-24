import numpy as np
import matplotlib.pyplot as plt

#===========Exercice 1===========
#=====question 1=====
def ex9f(x):
    y = np.cos(x**x)-np.sin(np.exp(x))
    return y

#=====question 2=====
x = np.linspace(0.5, 2.5, 201)
y = ex9f(x)
#print(y)

#=====question 3=====
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("ex9f function")
#plt.show()

#===========Exercice 2===========
##=====question 1=====
m = 100
pi1 = 0
for k in range(m+1):
    pi1 = pi1 + ((-1)**k / (2*k+1)) 

pi1 *= 4
#print(pi1)

##=====question 2=====
k2 = np.arange(101)
ind_k = ((-1)**k2 / (2*k2+1))
pi2 = 4 * np.sum(ind_k) 
#print(pi2) 

#print(np.isclose(pi1,pi2))

##=====question 3=====
def evalpi(mx):
    k = np.arange(mx + 1)
    terms = (-1.0)**k / (2*k + 1)
    aprx = 4 * np.sum(terms)
    return aprx

#testing
#print(evalpi(100))

##=====question 4=====
approximation = evalpi(100)
error = abs(approximation - np.pi)

#print("absolute error: ",error)

##=====question 5=====
for i in range(1, 6):
    m = 10**i
    approximation = evalpi(m)
    error = abs(approximation - np.pi)
    #print("m:", m, "\nwith an absolute error:", error, "\n")

##=====question 6=====
m6 = 9000
Q6_aprx = evalpi(m6)
er = abs(Q6_aprx - np.pi)
tolerance = 1e-4
while er > tolerance:
    previous_error = er
    m6 = m6 + 1
    Q6_aprx = Q6_aprx + 4 * (-1)**m6 / (2*m6 + 1)
    er = abs(Q6_aprx - np.pi)

print("first m meeting the tolerance:", m6, "\napproximation:", Q6_aprx, "\nabsolute error:", er, "\nnumber of terms:", m6 + 1)
print("previous m:", m6 - 1, "\nprevious error:", previous_error, "\nprevious m fails tolerance?", previous_error > tolerance)