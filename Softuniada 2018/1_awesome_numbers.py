number_one = int(input())
favorite_number = int(input())

result = ""

if all([number_one % favorite_number == 0, number_one < 0, number_one % 2 != 0]):
    result = "super special awesome"
elif all([number_one % favorite_number == 0, number_one < 0]) or all(
        [number_one % favorite_number == 0, number_one % 2 != 0]) or \
        all([number_one % 2, number_one < 0]):
    result = "super awesome"
elif any([number_one % favorite_number == 0, number_one < 0, number_one % 2 != 0]):
    result = "awesome"


else:
    result = "boring"


print(result)