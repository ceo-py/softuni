from project.movie_specification.movie import Movie
from project.user import User
from project.validation.validation import Validation


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        Validation.user_exists(username, self.users_collection)
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def __find_client(self, username:str):
        for c in self.users_collection:
            if c.username == username:
                return c

    def upload_movie(self, username: str, movie: Movie):
        Validation.user_not_registered(username, self.users_collection)
        client = self.__find_client(username)
        Validation.user_owned_movie(client, movie)
        Validation.movie_uploaded(movie, self.movies_collection)

        self.movies_collection.append(movie)
        client.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        client = self.__find_client(username)
        Validation.movie_not_uploaded(movie, self.movies_collection)
        Validation.user_owned_movie(client, movie)

        for attrib, new_value in kwargs.items():
            if attrib == "title":
                movie.title = new_value
            elif attrib == "year":
                movie.year = new_value
            elif attrib == "age_restriction":
                movie.age_restriction = new_value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        client = self.__find_client(username)
        Validation.movie_not_uploaded(movie, self.movies_collection)
        Validation.user_owned_movie(client, movie)
        movie_title = movie.title
        client.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie_title} movie."

    def like_movie(self, username: str, movie: Movie):
        client = self.__find_client(username)
        Validation.user_validate_owned_movie(client, movie)
        Validation.user_already_liked_movie(client, movie)

        movie.likes += 1
        client.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        client = self.__find_client(username)
        Validation.user_can_dislike(client, movie)
        movie.likes -= 1
        client.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."

        return '\n'.join(s.details() for s in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

    def __str__(self):
        output = ["All users: "]
        if not self.users_collection:
            output[0] += "No users."
        else:
            output[0] += ', '.join(u.username for u in self.users_collection)

        output.append("All movies: ")
        if not self.movies_collection:
            output[1] += "No movies."
        else:
            output[1] += ', '.join(u.title for u in self.movies_collection)

        return "\n".join(output)








