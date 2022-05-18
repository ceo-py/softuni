class Profile:
    def __init__(self, username, password):
        if len(username) not in range(5,16):
            raise ValueError("The username must be between 5 and 15 characters.")
        if len(password) < 7:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        for x in password:
            pass

