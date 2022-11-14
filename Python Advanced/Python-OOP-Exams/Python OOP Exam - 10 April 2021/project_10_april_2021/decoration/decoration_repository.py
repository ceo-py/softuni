class DecorationRepository:

    def __init__(self):
        self.decorations = []

    def add(self, decoration: object):
        self.decorations.append(decoration)

    def remove(self, decoration: object):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True

        return False
    
    def find_by_type(self, decoration_type: str):
        for d in self.decorations:
            if decoration_type == d.__class__.__name__:
                return d

        return "None"
