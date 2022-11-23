population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())

if minimum_wealth > sum(population) / len(population):
    print("No equal distribution possible")
    exit()

while any(x < minimum_wealth for x in population):
    max_number, number_to_change = max(population), min(population)
    index_max, index_min = population.index(max_number), population.index(number_to_change)
    added_value = minimum_wealth - number_to_change
    population[index_max] -= added_value
    population[index_min] += added_value

print(population)






# population = [int(n) for n in input().split(", ")]
# minimum_wealth = int(input())
#
# if sum(population) / len(population) < minimum_wealth:
#     print("No equal distribution possible")
#
# else:
#     for i in range(len(population)):
#         num = population[i]
#         if num < minimum_wealth:
#             result = minimum_wealth - num
#             max_number = max(population)
#             index_max_num = population.index(max_number)
#             check_number = max_number - result
#             population[i] = minimum_wealth
#             population[index_max_num] = check_number
#     print(population)
#
#



#
#
# population = [int(n) for n in input().split(", ")]
# minimum_wealth = int(input())
#
# distribution = True
# for ind, num in enumerate(population):
#     if num < minimum_wealth:
#         result = minimum_wealth - num
#         max_number = max(population)
#         index_max_num = population.index(max_number)
#         check_number = max_number - result
#         if check_number >= minimum_wealth:
#             population[ind] = minimum_wealth
#             population[index_max_num] = max_number - result
#         else:
#             distribution = False
#             print("No equal distribution possible")
#             break
#     else:
#         population[ind] = num
#
# if distribution:
#     print(population)
