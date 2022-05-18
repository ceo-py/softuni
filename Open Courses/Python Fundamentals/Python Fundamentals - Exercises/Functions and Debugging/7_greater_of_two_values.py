type_to_check = input()
first_check = input()
second_check = input()


def check_whats_bigger(type_, f, s):
    if type_ == "int":
        if int(f) > int(s):
            return f
        elif int(f) < int(s):
            return s
    elif type_ == "char":
        if ord(f) > ord(s):
            return f
        elif ord(f) < ord(s):
            return s
    elif type_ == "string":
        if f > s:
            return f
        elif f < s:
            return s


print(check_whats_bigger(type_to_check, first_check, second_check))
