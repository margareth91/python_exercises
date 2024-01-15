import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Przygotowanie bladzenia losowego i wyswietlenie punktow, gdy program pozostaje aktywny
rw = RandomWalk(50000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))
plt.scatter(
    rw.x_values,
    rw.y_values,
    c=point_numbers,
    cmap=plt.cm.Greens,
    edgecolors="none",
    s=1,
)
# # Podkreslenie pierwszego i ostatniego punktu
# plt.scatter(0, 0, c='green', edgecolors='none', s=100)
# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
# # Ukrycie osi
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)
# Okreslenie wielkosci ekranu
plt.figure(dpi=128, figsize=(10, 6))
plt.show()
