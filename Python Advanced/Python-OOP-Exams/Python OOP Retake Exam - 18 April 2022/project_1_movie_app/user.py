from project.validation.validation import Validation


class User:

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        Validation.username(value)
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validation.age_under(value)
        self.__age = value

    def __str__(self):
        output = [f"Username: {self.username}, Age: {self.age}", "Liked movies:"]
        if self.movies_liked:
            [output.append(m.details()) for m in self.movies_liked]
        else:
            output.append("No movies liked.")

        output.append("Owned movies:")

        if self.movies_owned:
            [output.append(m.details()) for m in self.movies_owned]
        else:
            output.append("No movies owned.")

        return "\n".join(output)

