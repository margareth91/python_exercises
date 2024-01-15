import matplotlib.pyplot as plt

input_values = [1,2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Zdefiniowanie tytulu wykresu i etykiet osi
plt.title("Kwadraty liczb", fontsize=24)
plt.xlabel("Wartosc", fontsize=14)
plt.ylabel("Kwadraty wartosci", fontsize=14)

# Zdefiniowanie wielkosci etykiet
plt.tick_params(axis='both', labelsize=14)

plt.show()
