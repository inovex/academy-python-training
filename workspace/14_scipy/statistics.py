## Statistics
import numpy as np
from scipy.stats import norm, poisson, ttest_ind

# generating random variates from a normal distribution
print(norm.rvs(size=3)) # [-1.05363041  3.03053898  1.25119302]
# computing the Probability Density Function of a normal distribution
print(norm.pdf([-1., 0, 1])) # [0.24197072 0.39894228 0.24197072]

## generating random variates from a poisson distribution
# generating random variates from a poisson distribution
print(poisson.rvs(size=3, mu=10)) # [ 1.41055722 -2.28832742  1.80195402]

# computing the Probability Mass Function of a Poisson distribution
## practical example:
# The average number of storms in your city is 2.5 per year.
# What is the probability that 2, 3, or 4 storm will hit your city next year?
historical_storms_avg = 2.5
k = np.array([2, 3, 4])
print(poisson.pmf(k, mu=historical_storms_avg)) # [0.25651562 0.21376302 0.13360189]

### performing a t-test
## compare the mean grades of students from two different Hogwarts houses
grades_gryffindor = [86, 100, 67, 45, 98, 82]
grades_slytherin = [89, 77, 36, 99, 99, 79]

t_stat, p_value = ttest_ind(grades_gryffindor, grades_slytherin)
print(t_stat) # -0.013032814931570842
print(p_value) # 0.9898579607088525