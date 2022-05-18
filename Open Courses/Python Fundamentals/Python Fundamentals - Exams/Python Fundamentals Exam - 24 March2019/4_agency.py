from abc import ABC, abstractmethod


class Apartment(ABC):
    def __init__(self, id, rooms, bathrooms, square_meters, price, is_hired=False):
        self.id = id
        self.rooms = int(rooms)
        self.bathrooms = int(bathrooms)
        self.square_meters = float(square_meters)
        self.price = float(price)
        self.is_hired = is_hired

    @abstractmethod
    def __str__(self):
        pass

    def info(self):
        return f'{self.rooms} rooms place with {self.bathrooms} bathroom/s.\n{self.square_meters} sq. meters for {self.price} lv.'


class OfficeApartment(Apartment):
    def __str__(self):
        return self.info()


class LivingApartment(Apartment):
    def __str__(self):
        return self.info()


data = input()
apartments = []

while not data == 'start_selling':
    try:
        apartment = eval(data)
        apartments.append(apartment)
    except Exception as exception:
        print(exception)

    data = input()

data = input()

while not (data == 'free' or data == 'taken'):
    action = data.split()[0]
    id = data.split()[1]

    all_apartments_ids = list(map(lambda ap: ap.id, apartments))
    taken_list = list(map(lambda ap: ap.id, list(filter(lambda apartment: apartment.is_hired == True, apartments))))
    free_list = list(map(lambda ap: ap.id, list(filter(lambda apartment: apartment.is_hired == False, apartments))))

    if not id in all_apartments_ids:
        print(f'Apartment with id - {id} does not exist!')
    else:
        if id in taken_list:
            print(f'Apartment with id - {id} is already taken!')
        else:
            apartment = list(filter(lambda ap: ap.id == id, apartments))[0]
            if action == 'rent' and isinstance(apartment, LivingApartment):
                print(f'Apartment with id - {id} is only for selling!')
            elif action == 'buy' and isinstance(apartment, OfficeApartment):
                print(f'Apartment with id - {id} is only for renting!')
            else:
                apartment.is_hired = True

    data = input()

query_list = []
ordered_query_list = []

if data == 'taken':
    query_list = list(filter(lambda ap: ap.is_hired == True, apartments))
    ordered_query_list = sorted(query_list, key=lambda ap: (ap.price, -ap.square_meters))
else:
    query_list = list(filter(lambda ap: ap.is_hired == False, apartments))
    ordered_query_list = sorted(query_list, key=lambda ap: (-ap.price, -ap.square_meters))

if ordered_query_list:
    for apartment in ordered_query_list:
        print(apartment)
else:
    print('No information for this query')









