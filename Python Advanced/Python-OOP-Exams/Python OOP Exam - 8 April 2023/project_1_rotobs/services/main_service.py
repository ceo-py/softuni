from project.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name: str, capacity: int = 30):
        super().__init__(name, capacity)
        self.type = 'MainService'

    def details(self):
        output = f'{self.name} Main Service:\nRobots: '
        if self.robots:
            output += ' '.join(r.name for r in self.robots)
        else:
            output += 'none'
        return output

