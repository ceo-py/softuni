class Validation:

    @staticmethod
    def username(name: str):
        if name == "":
            raise ValueError("Invalid username!")

    @staticmethod
    def age_under(age: int):
        if age < 6:
            raise ValueError("Users under the age of 6 are not allowed!")

    @staticmethod
    def movie_title(title: str):
        if title == "":
            raise ValueError("The title cannot be empty string!")

    @staticmethod
    def movie_year(year: int):
        if year < 1888:
            raise ValueError("Movies weren't made before 1888!")

    @staticmethod
    def movie_owner(owner):
        if owner.__class__.__name__ != "User":
            raise ValueError("The owner must be an object of type User!")

    @staticmethod
    def age_restriction(age: int, genre_class):
        if age < genre_class._age_restriction:
            raise ValueError(
                f"{genre_class.__class__.__name__} movies must be restricted for "
                f"audience under {genre_class._age_restriction} years!")

    @staticmethod
    def user_exists(username: str, users_list_class):
        if any(username == u.username for u in users_list_class):
            raise Exception("User already exists!")

    @staticmethod
    def user_not_registered(username: str, users_list_class):
        if all(username != u.username for u in users_list_class):
            raise Exception("This user does not exist!")

    @staticmethod
    def user_owned_movie(client_class, movie_class):
        if movie_class.owner.username != client_class.username:
            raise Exception(f"{client_class.username} is not the owner of the movie {movie_class.title}!")

    @staticmethod
    def movie_uploaded(movie_class, movies: list):
        if movie_class in movies:
            raise Exception("Movie already added to the collection!")

    @staticmethod
    def movie_not_uploaded(movie_class, movies: list):
        if movie_class not in movies:
            raise Exception(f"The movie {movie_class.title} is not uploaded!")

    @staticmethod
    def user_validate_owned_movie(client_class, movie_class):
        if movie_class in client_class.movies_owned:
            raise Exception(f"{client_class.username} is the owner of the movie {movie_class.title}!")

    @staticmethod
    def user_already_liked_movie(client_class, movie_class):
        if movie_class in client_class.movies_liked:
            raise Exception(f"{client_class.username} already liked the movie {movie_class.title}!")

    @staticmethod
    def user_can_dislike(client_class, movie_class):
        if movie_class not in client_class.movies_liked:
            raise Exception(f"{client_class.username} has not liked the movie {movie_class.title}!")

