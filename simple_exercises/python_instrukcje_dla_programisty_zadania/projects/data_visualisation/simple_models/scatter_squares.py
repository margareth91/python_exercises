import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# Zdefiniowanie tytulu wykresu i etykiet osi
plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartosc", fontsize=14)
plt.ylabel("Kwadraty wartosci", fontsize=14)

# Zdefiniowanie wartosci etykiet
plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
plt.savefig('squares_plot.png')
