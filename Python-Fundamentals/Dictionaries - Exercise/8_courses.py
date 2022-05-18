command = input()

school_information = {}
while command != "end":
    command = command.split(" : ")
    language_name = command[0]
    studen_name = command[1]
    school_information[language_name] = school_information.get(language_name, {})
    school_information[language_name][studen_name] = studen_name
    command = input()

for lang in school_information:
    print(f"{lang}: {len(school_information[lang])}")
    for key, value in school_information[lang].items():
        print(f"-- {value}")
