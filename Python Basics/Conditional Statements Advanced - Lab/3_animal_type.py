animal = input()

output = ' unknown'

if animal in 'crocodile, tortoise, snake':
    output = 'reptile'

elif animal == 'dog':
    output = 'mammal'

print(output)



# animal = input()
#
# type_animal = {
#     "dog": "mammal",
#     "crocodile": "reptile",
#     "tortoise": "reptile",
#     "snake": "reptile"
#     }
#
# print(type_animal.get(animal, 'unknown'))