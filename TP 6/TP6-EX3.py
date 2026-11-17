import numpy as np
#=====question 1=====
n = 8000
rng = np.random.default_rng(1)
z = rng.standard_normal(n)
y = 2*z + 10**9
var_y = (np.sum(y**2) - (1/n)*np.sum(y)**2) / (n - 1)
rel = abs(var_y - 4) / 4
print(f"estimate variance: {var_y}")
print(f"relative deviation: {rel}")

#=====question 2=====
for k in range(11):
    d = 10**k
    x = y - d

    var_x = (np.sum(x**2) - (1/n)*np.sum(x)**2) / (n - 1)

    rel2 = abs(var_x - 4) / 4

    print("d =", d)
    print("estimated variance:", var_x)
    print("Relative deviation:", rel2)
    print()

#=====question 3=====
mean_y = np.sum(y) / n
var_3 = np.sum((y - mean_y)**2) / (n - 1)
rel3 = abs(var_3 - 4) / 4

print("estimated variance:", var_3)
print("relative deviation:", rel3)

#=====question 4=====
#the one pass formula can accumulate the sum and sum of squares in a single traversal it needs little storage but can suffer cancellation when the mean is large relative to the spread

#The two pass algorithm first calculates the mean then sums the squared deviations from it, it is more accurate but requires storing