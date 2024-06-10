import matplotlib.pyplot as plt
import numpy as np

# Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.show()  # does not work inside codeanywhere
plt.savefig("figures/basic_line_plot.png")
plt.close()

# adding another line to the plot
plt.plot(x, y, x, -.5*y)
plt.savefig("figures/basic_multiline_plot.png")
plt.close()

# Scatter Plot
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y)
plt.savefig("figures/basic_scatter_plot.png")
plt.close()

# Bar Plot
quidditch_teams = ["Gryffindor", "Slytherin",
                   "Hufflepuff", "Ravenclaw"]
num_championships = [26, 22, 8, 12]
plt.bar(quidditch_teams, num_championships)
plt.savefig("figures/basic_bar_plot.png")
plt.close()

# Histogram
alchemy_grades = np.random.normal(0, 10, 1000)
plt.hist(alchemy_grades, bins='auto')
plt.savefig("figures/basic_hist.png")
