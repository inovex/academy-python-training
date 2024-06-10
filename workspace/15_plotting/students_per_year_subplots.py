import matplotlib.pyplot as plt

houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
years = [1991, 1992, 1993, 1994]
students_1991 = [50, 30, 20, 20]
students_1992 = [60, 40, 30, 20]
students_1993 = [70, 50, 40, 30]
students_1994 = [80, 60, 50, 40]

fig, ax = plt.subplots(2, 2, figsize=(10, 8), sharey=True)
ax[0, 0].bar(years, students_1991, color='blue')
ax[0, 1].bar(years, students_1992, color='green')
ax[1, 0].bar(years, students_1993, color='red')
ax[1, 1].bar(years, students_1994, color='purple')

ax[0, 0].set_title('1991')
ax[0, 1].set_title('1992')
ax[1, 0].set_title('1993')
ax[1, 1].set_title('1994')

for i in range(2):
    for j in range(2):
        ax[i, j].set_xlabel('House')
        ax[i, j].set_ylabel('Number of students')
        ax[i, j].set_xticks(years)
        ax[i, j].set_xticklabels(houses, rotation=45)

plt.suptitle("Number of Students per Year and House")
plt.tight_layout()
plt.show()
plt.savefig("figures/students_per_year_subplots.png")
