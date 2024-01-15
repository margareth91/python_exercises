import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x ** 3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolors='none', s=25)

# Zdefiniowanie tytulu wykresu i etykiet osi
plt.title("Szesciany liczb", fontsize=24)
plt.xlabel("Wartosc", fontsize=14)
plt.ylabel("Szescian wartosci", fontsize=14)

# Zdefiniowanie wartosci etykiet
plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
plt.savefig('cubes_plot.png')
