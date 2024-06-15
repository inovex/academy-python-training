# 1. Use scipy.stats.norm to generate a random sample of 100 variates from a normal distribution with a mean of 0 and a standard deviation of 1
# 2. Use scipy.linalg to solve the following linear equation:
#       3x + 2y = 9
#        x - y = 1
# 3. Given the following sample data points, use scipy.interpolate.interp1d with a cubic interpolation method
#    to find the y value for x=3.5
#       - sample = [(1,2), (2,3), (3,4), (4,5)]
# 4. Minimize the following function using scipy.optimize.minimize. Make an initial guess of x1=1 and x2=1.
#    Print the minimum value and the return value of the function at the minimum.
#    f((x1, x2) = x1**2 + x[2]**2

from scipy.stats import norm
from scipy import linalg
from scipy.interpolate import interp1d
from scipy.optimize import minimize

## 1.
# loc defines mean, scale defines std, size defines number of random variates
random_sample = norm.rvs(loc=0, scale=1, size=100)
print(random_sample)

## 2.
A = [[3, 2], [1, -1]]
b = [9, 1]

# solve the equation
x, y = linalg.solve(A, b)
print("x:", x)
print("y:", y)

## 3.
sample = [(1,2), (2,3), (3,4), (4,5)]
x = [x[0] for x in sample]
y = [x[1] for x in sample]

cubic_interp = interp1d(x, y, kind='cubic')

# find y value for a given x value
x_interp = 3.5
y_interp = cubic_interp(x_interp)
print(f"Interpolated value y for x = {x_interp}: {y_interp}")

## 4.
def f(x):
    return x[0]**2 + x[1]**2

# initial guess x0
x0 = [1, 1]

# minimizing f(x)
res = minimize(f, x0=x0)

print("Minimum value:", res.fun)
print("Values of the variables at the minimum:", res.x)
