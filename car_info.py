def car_info(manufacturer, model, **info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in info.items():
        car[key] = value
    return car

carr = car_info('subaru', 'outback', color='blue', tow_package=True)

print(carr)
