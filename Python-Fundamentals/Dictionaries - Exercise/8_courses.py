command = input()

school_information = {}
while command != "end":
    language_name, student_name = command.split(" : ")
    school_information[language_name] = school_information.get(language_name, {})
    school_information[language_name][student_name] = student_name
    command = input()

for lang in school_information:
    print(f"{lang}: {len(school_information[lang])}")
    for key, value in school_information[lang].items():
        print(f"-- {value}")
