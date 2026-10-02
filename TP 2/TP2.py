# Imports
import numpy as np
import matplotlib.pyplot as plt

#for each questions in the exercices i will place # so it wont run everything

#OBJECTIVES
##question 1
#the formula translated into code -> np.sin(2.0**(-1) * np.pi)

#start with an empty matrix of 10 x 1 to fill in
v = np.zeros((10, 1))

#filling each row of v with the formula for the respective i
for i in range(1,11):
    v[i-1, 0] = np.sin(2**(-i)*np.pi)

###print for the Q1
#print(v, "\n")

##question 2
#since we cant do a loop we directly prepare all of i from 1 to 10
i = np.arange(1,11)
i = i.reshape((10,1)) #reshape it to 10x1 to easily execute the formula on each row
v2 = np.sin(2.0**(-i) * np.pi)

###print for Q2
#print(v2)

#Exercice 1
##question 1
x = np.arange(3,13) #vector with the values from 3 to 12
ttl_sum = 0 
for x_value in x:
    ttl_sum = ttl_sum + x_value

##question 2
ttl_prod = 1
for x_value in x:
    ttl_prod = ttl_prod * x_value

###print for both question 1 and question 2 (sum and product)
#print("the total sum of the elements in the vector is: \n",ttl_sum, "\n","the total product of the elements of the vector is: \n",ttl_prod)

###verifying the results with the use of numpy after executing we can notice we get the same values as the loops
#print(np.sum(x)," \n", np.prod(x)) 


#Exercice 2
x1 = np.arange(0, 41, 4)

#question 1
n = len(x1)
#make a new vector to place the results after running the formula on it
y = np.zeros(n)
for i in range(n):
    y[i] = 3*x1[i]**2+2*x1[i]-1

#no loop
yf =3*x1**2+2*x1-1

###print("with loop:", y)
###print("without loop:", yf)
###print("same values -> ", np.allclose(y, yf))

#question 2
z = np.zeros((n-2))
for i in range(n-2):
    z[i] = y[i]+y[i+1]+y[i+2]

###print(z)

#question 3
f = np.zeros((len(z)))
for i in range(n-2):
    f[i] = abs(z[i])

###print(f)

#question 4
g = np.zeros((len(z)))
for i in range(n-2):
    g[i] = np.log(abs(z[i]))

###print(g)


###question 5
rng = np.random.default_rng(0)
A = rng.uniform(size=(3, 4))
A_og = A.copy()

#print(A, "\n", A_og) #to check if it works
for i in range(3):
    for j in range(4):
        if A[i,j] < 0.2:
            A[i,j] = 0
        else:
            A[i,j] = 1

v = (A_og >= 0.2).astype(int)
###print(A)
###print("result verification: \n", np.array_equal(A, v))

#Exercice 3
import numpy as np
X = np.arange(1, 11)
Y = np.array([3, 1, 5, 6, 8, 2, 9, 4, 7, 0])

#gives True if the value in x in is inbetween 3 and 8 (excluding 3 and 8)
#print((X > 3) & (X < 8))

#get all the values that are above 5
#print(X[X > 5])

#get the values of y at positions where x <= 4
#print(Y[X <= 4])

#get values of x below 2 or equal/above 8
#print(X[(X < 2) | (X >= 8)])

#get values of y at those position in respect to the boolean demand
#print(Y[(X < 2) | (X >= 8)])

#trying to select values of x if y is negative
#print(X[Y < 0])


