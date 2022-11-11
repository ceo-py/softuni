from project.movie_specification.movie import Movie


class Fantasy(Movie):
    _age_restriction = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)
