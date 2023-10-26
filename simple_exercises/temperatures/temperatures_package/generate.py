
import random


temperature_days = []


def temperature_for_a_day():
    while len(temperature_days) < 30:
        day_temperature = int(random.randint(-20, 30))
        temperature_days.append(day_temperature)

    print(f"Zbior temperatur z ostatniego miesiaca: {temperature_days}.")
    return temperature_days
