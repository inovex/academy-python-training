import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, axs = plt.subplots(nrows=2, ncols=1)
fig.suptitle("Vertically stacked subplots")
axs[0].plot(x, y)
axs[1].plot(x, -y)
plt.show()
plt.savefig("figures/plt_subplots.png")
