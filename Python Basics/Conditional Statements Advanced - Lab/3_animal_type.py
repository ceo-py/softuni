animal = input()

type_anymal = {
    "dog": "mammal",
    "crocodile": "reptile",
    "tortoise": "reptile",
    "snake": "reptile"
    }

if animal in type_anymal:
    print(type_anymal[animal])
else:
    print("unknown")