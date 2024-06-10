## Optimization
import scipy as sp 

### minimize
from scipy.optimize import minimize

# minimizing f(x) = (x - 4)^2 
def f(x):
    return (x - 4)**2

res = minimize(f, x0=2) # you have to make an initial "guess" x0
print(res.x) # [3.99999998]

### Nelder-Mead Simplex algorithm
# - finding the min/max of an objective function in a multidimensional space
from scipy.optimize import minimize
import numpy as np 
# minimizing f([x1, x2]) = (1 - x1)^2
def f(x):
    return 0.5*(4 - x[0])**2

x0 = np.array([1, 1, 1])
res = minimize(f, x0=x0, method='nelder-mead')
print(res.x) # [4.00000623 -0.45398315 -0.70141322]
print(res.fun) # 1.940193957557011e-11

### Minimization with constraints