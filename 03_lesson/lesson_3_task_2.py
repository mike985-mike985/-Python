from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S21", "+79242718265"),

    Smartphone("Samsung", "Galaxy S22", "+79242718264"),

    Smartphone("Samsung", "Galaxy S23", "+79242718263"),

    Smartphone("Samsung", "Galaxy S24", "+79242718262"),

    Smartphone("Samsung", "Galaxy S25", "+79242718261")
]

for smartphone in catalog:

    print(f"{smartphone.phone_brand} - {smartphone.phone_model} - "
          f"{smartphone.subscription_number}")
