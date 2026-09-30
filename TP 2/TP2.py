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

#print(v, "\n")

##question 2
#since we cant do a loop we directly prepare all of i from 1 to 10
i = np.arange(1,11)
i = i.reshape((10,1)) #reshape it to 10x1 to easily execute the formula on each row
v2 = np.sin(2.0**(-i) * np.pi)
#print(v2)