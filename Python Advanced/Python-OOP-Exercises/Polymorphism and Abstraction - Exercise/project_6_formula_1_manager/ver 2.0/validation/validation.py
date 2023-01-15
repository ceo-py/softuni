class Validation:

    @staticmethod
    def less_than(num: int, target_num: int, message: str):
        if num < target_num:
            raise ValueError(message)

    @staticmethod
    def item_duplicate(item: str, collection: dict, message: str):
        if item not in collection:
            raise ValueError(message)

    @staticmethod
    def team_registered(teams: dict, message: str):
        if any(t is None for t in teams):
            raise Exception(message)
