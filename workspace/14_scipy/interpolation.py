# source: https://docs.scipy.org/doc/scipy/tutorial/interpolate/1D.html
## interpolation

### linear and cubic interpolation
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import os

x = np.linspace(0, 10, 20)
y = np.cos(-x**2 / 9.0)

# construct the interpolation
xnew = np.linspace(0, 10, 1000)
lin_interp = interp1d(x, y, kind='linear')
cub_interp = interp1d(x, y, kind='cubic')
y_linear = lin_interp(xnew)
y_cubic = cub_interp(xnew)

plt.plot(x, y, 'o', xnew, y_linear, '-', xnew, y_cubic, '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')

plt.savefig('workspace/14_scipy/figures/interpolation.png')

