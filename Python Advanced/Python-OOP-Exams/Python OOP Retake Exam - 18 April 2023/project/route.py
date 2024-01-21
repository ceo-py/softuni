from project.validation.validation import Validation


class Route:
    MIN_LENGTH = 1.00

    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id
        self.is_locked = False

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, value):
        Validation.empty_or_white_space(value, 'Start point cannot be empty!')
        self.__start_point = value

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, value):
        Validation.empty_or_white_space(value, 'End point cannot be empty!')
        self.__end_point = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        Validation.number_is_less_than(value, Route.MIN_LENGTH, f'Length cannot be less than {Route.MIN_LENGTH:.2f} kilometer!')
        self.__length = value
