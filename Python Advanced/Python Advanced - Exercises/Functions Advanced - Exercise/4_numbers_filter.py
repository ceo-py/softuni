def even_odd_filter(**kwargs):
    result = {}
    for type_numbers, numbers in kwargs.items():
        if type_numbers == "even":
            result[type_numbers] = [x for x in numbers if x % 2 == 0]
        elif type_numbers == "odd":
            result[type_numbers] = [x for x in numbers if x % 2 != 0]
    return dict(sorted(result.items()))