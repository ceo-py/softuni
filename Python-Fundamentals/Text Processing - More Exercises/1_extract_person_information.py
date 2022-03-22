number_strings = int(input())

for _ in range(number_strings):
    test_string = input()
    # if all([test_string.count("@") == 1, test_string.count("|") == 1,
    #         test_string.count("#") == 1, test_string.count("*") == 1]):
    name = test_string[test_string.index("@") + 1:test_string.index("|")]
    age = test_string[test_string.index("#") + 1:test_string.index("*")]
    print(f"{name} is {age} years old.")
