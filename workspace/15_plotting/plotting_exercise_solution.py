import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# sns.set_theme()

# Matplotlib
# 1. Given the following lists, create a bar plot of Hogwarts House Points.
#    Make sure to add axes-labels and a title.
houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
points = [715, 517, 470, 482]

plt.bar(houses, points)
plt.title("Hogwarts House Points")
plt.xlabel("House")
plt.ylabel("# Points")
plt.savefig("figures/exercise/house_points_plt.png")
plt.close()

# 2. Given the following lists depicting the House Points over time, create a line plot.
#    Add axes-labels, a title, and a legend with labels for the houses.

years = np.arange(1991, 1998)
gryffindor_points = [200, 180, 225, 300, 325, 310, 375]
ravenclaw_points = [225, 250, 200, 225, 175, 200, 175]
slytherin_points = [150, 100, 125, 175, 175, 175, 200]
hufflepuff_points = [100, 125, 100, 75, 75, 100, 50]

plt.plot(years, gryffindor_points, "-", label="Gryffindor")
plt.plot(years, ravenclaw_points, "--", label="Ravenclaw")
plt.plot(years, slytherin_points, ":", label="Slytherin")
plt.plot(years, hufflepuff_points, "-.", label="Hufflepuff")

plt.title("Hogwarts House Points over Time")
plt.xlabel("Year")
plt.ylabel("# Points")
plt.legend()
plt.savefig("figures/exercise/points_over_time_plt.png")
plt.close()
