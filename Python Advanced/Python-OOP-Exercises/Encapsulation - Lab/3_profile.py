class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if 5 <= len(value) <= 15:
            self.__username = value
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) >= 8 and sum(1 for x in value if x.isdigit()) >= 1 and \
                sum(1 for x in value if x.isupper()):
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters "
                             "with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and ' \
               f'password: {"*" * len(self.__password)}'



# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)

profile_with_invalid_username = Profile('Too_long_username', 'Any')
