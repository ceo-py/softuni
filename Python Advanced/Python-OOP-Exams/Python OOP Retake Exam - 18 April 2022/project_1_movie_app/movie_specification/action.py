from project.movie_specification.movie import Movie


class Action(Movie):
    _age_restriction = 12

    def __init__(self, title: str, year: int, owner: object, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

