from abc import ABC, abstractmethod
from project.validation.validation import Validation

class BaseService(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []
       
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        Validation.empty_or_white_space(value, 'Service name cannot be empty!')
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        Validation.less_than_or_equal_to(value, 0, 'Service capacity cannot be less than or equal to 0!')
        self.__capacity = value


    def can_be_add(self):
        Validation.can_be_add(self.capacity, len(self.robots), 'Not enough capacity for this robot!')

    def find_robot(self, robot_name: str):
        Validation.item_exist(robot_name, self.robots, 'No such robot in this service!')

    def remove_robot(self, robot_name: str):
        for i in range(len(self.robots)):
            if self.robots[i].name == robot_name:
                return self.robots.pop(i)

    def feed_robots(self):
        for r in self.robots:
            r.eating()

    def calculate_robot_price(self) -> int:
        return sum([r.price for r in self.robots])

    @abstractmethod
    def details(self):
        pass