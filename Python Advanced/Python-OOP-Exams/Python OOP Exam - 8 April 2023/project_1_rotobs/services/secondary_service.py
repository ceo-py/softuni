from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str, capacity: int = 15):
        super().__init__(name, capacity)
        self.type = 'SecondaryService'

    def details(self):
        output = f'{self.name} Secondary Service:\nRobots: '
        if self.robots:
            output += ' '.join(r.name for r in self.robots)
        else:
            output += 'none'
        return output