def get_info(**kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"
    #eturn f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))