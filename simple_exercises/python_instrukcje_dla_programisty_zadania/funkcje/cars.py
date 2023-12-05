def make_cars_list(make, model, **car_info):
    car_profile = {}
    car_profile['make'] = make
    car_profile['model'] = model
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile


car1 = make_cars_list('bmw', 'x1', color='red', car_mileage='200000 km')
print(car1)
