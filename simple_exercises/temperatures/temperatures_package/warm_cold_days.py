
from generate import temperature_days


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