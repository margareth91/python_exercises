from die import Die
import pygal

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# Wizualizacja wynikow
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania pojedyncza koscia D6 tysiac razy"
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = "Wynik"
hist.y_title = "Czestotliwosc wystepowania wartosci"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
