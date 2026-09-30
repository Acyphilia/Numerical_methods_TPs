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
xf = np.zeros(n)
for i in range(n):
    xf[i] = 3*x1[i]**2+2*x1[i]-1

#no loop
xf1 =3*x1**2+2*x1-1

###print("with loop:", xf)
###print("without loop:", xf1)
###print("same values => ", np.allclose(xf, xf1))