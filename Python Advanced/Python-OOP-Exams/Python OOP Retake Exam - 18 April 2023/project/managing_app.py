from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []

    @staticmethod
    def __get_item(attribute: str, description: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == description:
                return obj

    def __get_route(self, start_point: str, end_point: str):
        for obj in self.routes:
            if obj.start_point == start_point and obj.end_point == end_point:
                return obj

    @property
    def __get_route_id(self):
        return len(self.routes) + 1

    @property
    def __get_vehicles_for_repair(self):
        return sorted([v for v in self.vehicles if v.is_damaged], key=lambda v: (v.brand, v.model))

    @property
    def vehicle_types(self):
        return {
            'PassengerCar': PassengerCar,
            'CargoVan': CargoVan,
        }

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.__get_item('driving_license_number', driving_license_number, self.users)

        if user:
            return f'{driving_license_number} has already been registered to our platform.'

        self.users.append(User(first_name, last_name, driving_license_number))
        return f'{first_name} {last_name} was successfully registered under DLN-{driving_license_number}'

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.vehicle_types:
            return f'Vehicle type {vehicle_type} is inaccessible.'

        vehicle = self.__get_item('license_plate_number', license_plate_number, self.vehicles)

        if vehicle:
            return f'{license_plate_number} belongs to another vehicle.'

        self.vehicles.append(self.vehicle_types[vehicle_type](brand, model, license_plate_number))
        return f'{brand} {model} was successfully uploaded with LPN-{license_plate_number}.'

    def allow_route(self, start_point: str, end_point: str, length: float):
        route = self.__get_route(start_point, end_point)

        if not route or route.length > length:
            if route:
                route.is_locked = True

            self.routes.append(Route(start_point, end_point, length, self.__get_route_id))
            return f'{start_point}/{end_point} - {length} km is unlocked and available to use.'

        if route.length == length:
            return f'{start_point}/{end_point} - {length} km had already been added to our platform.'

        if route.length < length:
            return f'{start_point}/{end_point} shorter route had already been added to our platform.'

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self.__get_item('driving_license_number', driving_license_number, self.users)
        vehicle = self.__get_item('license_plate_number', license_plate_number, self.vehicles)
        route = self.__get_item('route_id', route_id, self.routes)

        if user.is_blocked:
            return f'User {driving_license_number} is blocked in the platform! This trip is not allowed.'

        if vehicle.is_damaged:
            return f'Vehicle {license_plate_number} is damaged! This trip is not allowed.'

        if route.is_locked:
            return f'Route {route_id} is locked! This trip is not allowed.'

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        vehicles = self.__get_vehicles_for_repair[:count]

        for v in vehicles:
            v.recharge()
            v.change_status()

        return f'{len(vehicles)} vehicles were successfully repaired!'

    def users_report(self):
        output = ['*** E-Drive-Rent ***'] + [str(u) for u in sorted(self.users, key=lambda x: -x.rating)]
        return "\n".join(output)
