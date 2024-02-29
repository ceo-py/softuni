from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from project.validation.validation import Validation


class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []

    @property
    def correct_services(self):
        return {
            'MainService': MainService,
            'SecondaryService': SecondaryService
        }

    @property
    def correct_robots(self):
        return {
            'MaleRobot': MaleRobot,
            'FemaleRobot': FemaleRobot
        }
    @staticmethod
    def __get_item(item_to_found: str, collection: list) -> object:
        for i in collection:
            if i.name == item_to_found:
                return i



    def add_service(self, service_type: str, name: str) -> str:
        Validation.is_type_valid(service_type, self.correct_services, 'Invalid service type!')
        current_service = self.correct_services[service_type](name)
        self.services.append(current_service)
        return f'{service_type} is successfully added.'


    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        Validation.is_type_valid(robot_type, self.correct_robots, 'Invalid robot type!')
        current_robot = self.correct_robots[robot_type](name, kind, price)
        self.robots.append(current_robot)
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self.__get_item(robot_name, self.robots)
        service = self.__get_item(service_name, self.services)

        if not robot.can_be_add(service.type):
            return 'Unsuitable service.'
        service.can_be_add()

        service.robots.append(robot)
        self.robots.remove(robot)

        return f'Successfully added {robot_name} to {service_name}.'

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = self.__get_item(service_name, self.services)
        service.find_robot(robot_name)

        self.robots.append(service.remove_robot(robot_name))
        return f'Successfully removed {robot_name} from {service_name}.'


    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self.__get_item(service_name, self.services)
        service.feed_robots()

        return f'Robots fed: {len(service.robots)}.'

    def service_price(self, service_name: str) -> str:
        service = self.__get_item(service_name, self.services)
        total_price = service.calculate_robot_price()

        return f'The value of service {service_name} is {total_price:.2f}.'

    def __str__(self) -> str:
        output = []
        for s in self.services:
            output.append(s.details())

        return '\n'.join(output)

