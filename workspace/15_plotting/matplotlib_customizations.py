import matplotlib.pyplot as plt

# Labels and Titles
num_students = [489, 512, 622, 817, 803, 915, 997]
years = [2000, 2002, 2004, 2006, 2008, 2010, 2012]
plt.plot(years, num_students)
plt.xlabel("Year")
plt.ylabel("Number of Students")
plt.title("Number of Hogwarts Students per Year")
plt.savefig("figures/plt_labels_titles.png")
plt.close()

# Legends
num_first_year_students = [80, 103, 107, 164,
                           133, 189, 219]
plt.plot(years, num_students, '-', years, num_first_year_students, '--')
plt.legend(["all students", "first-year students"], loc="best")
plt.title("Number of Hogwarts Students per Year")
plt.xlabel("Year")
plt.ylabel("# Students")
plt.savefig("figures/plt_legend.png")
plt.close()

# Colors and markers
num_students = [489, 512, 622, 817, 803, 915, 997]
years = [2000, 2002, 2004, 2006, 2008, 2010, 2012]
plt.plot(years, num_students, linestyle="-", color="red", marker="o")
plt.plot(years, num_first_year_students,
         linestyle="--", color="green", marker="^")
plt.legend(["all students", "first-year students"], loc="best")
plt.savefig("figures/plt_colors_markers.png")
plt.close()

# Alternatively, we can use format-strings
plt.plot(years, num_students, "r-o",
         years, num_first_year_students, "g--^")
plt.legend(["all students", "first-year students"], loc="best")
plt.savefig("figures/plt_colors_markers.png")
plt.close()
