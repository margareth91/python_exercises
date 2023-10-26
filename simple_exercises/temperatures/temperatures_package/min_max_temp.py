
from generate import temperature_days


def min_max_temperature():
    min_temperature = min(temperature_days)
    max_temperature = max(temperature_days)

    print(f"Najnizsza temperatura to {min_temperature}, a najwyzsza {max_temperature}.")