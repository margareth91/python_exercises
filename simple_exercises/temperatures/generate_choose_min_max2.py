
# temp -20/20, ile dni cieplych ile zimnych

import random


temperature_days = []


def temperature_for_a_day():
    while len(temperature_days) < 30:
        day_temperature = int(random.randint(-20, 30))
        temperature_days.append(day_temperature)

    print(f"Zbior temperatur z ostatniego miesiaca: {temperature_days}.")
    return temperature_days


def min_max_temperature():
    min_temperature = min(temperature_days)
    max_temperature = max(temperature_days)

    print(f"Najnizsza temperatura to {min_temperature}, a najwyzsza {max_temperature}.")


def warm_cold_days():
    warm_days = []
    for temperature_day in temperature_days:
        if temperature_day > 20:
            warm_days.append(temperature_day)
    print(f"W zeszlych 30 dniach bylo {len(warm_days)} cieplych dni, a ich temperatury to: {warm_days}.")

    cold_days = []
    for temperature_day in temperature_days:
        if temperature_day < 0:
            cold_days.append(temperature_day)
    print(f"W zeszlych 30 dniach bylo {len(cold_days)} zimnych dni, a ich temperatury to: {cold_days}.")


if __name__ == '__main__':
    temperature_for_a_day()
    min_max_temperature()
    warm_cold_days()
