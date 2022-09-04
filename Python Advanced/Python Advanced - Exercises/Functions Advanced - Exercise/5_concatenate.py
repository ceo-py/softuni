def concatenate(*args, **kwargs):
    main_string = ''.join(args)
    for key_to_check, string_to_change in kwargs.items():
        if key_to_check in main_string:
            main_string = main_string.replace(key_to_check, string_to_change)
    return main_string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))