import numpy as np

# 1. Given the following lists, create a bar plot of Hogwarts House Points.
#    Make sure to add axes-labels and a title.
houses = ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff']
points = [715, 517, 470, 482]

# 2. Given the following lists depicting the House Points over time, create a line plot. 
#    Add axes-labels, a title, and a legend with labels for the houses.

years = np.arange(1991, 1998)
gryffindor_points = [200, 180, 225, 300, 325, 310, 375]
ravenclaw_points = [225, 250, 200, 225, 175, 200, 175]
slytherin_points = [150, 100, 125, 175, 175, 175, 200]
hufflepuff_points = [100, 125, 100, 75, 75, 100, 50]
