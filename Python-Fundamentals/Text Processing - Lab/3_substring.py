string_one = input()
string_two = input()

while string_one in string_two:
    string_two = string_two.replace(string_one, "")

print(string_two)
