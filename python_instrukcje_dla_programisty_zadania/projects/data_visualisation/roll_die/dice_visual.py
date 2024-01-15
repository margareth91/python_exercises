from die import Die
import pygal

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)


frequencies = []

max_result = die1.num_sides + die2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)


# Wizualizacja wynikow
hist = pygal.Bar()
hist.force_uri_protocol = "http"

hist.title = "Wynik rzucania dwiema koscmi D6 tysiac razy"
hist.x_labels = [labels for labels in range(2, max_result + 1)]
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Wynik"
hist.y_title = "Czestotliwosc wystepowania wartosci"

hist.add("D6 + D6", frequencies)
hist.render_to_file("dice_visual2.svg")
