import re

person_information = {}
main_string = input()

pattern = re.compile(r"name is ([A-Z][a-z]+ [A-Z][a-z]+\.).+ (\d\d) years .+ on (\d\d-\d\d-\d\d\d\d\.)")

while main_string != "make migrations":
    matches = pattern.finditer(main_string)
    for show in matches:
        person_information[show[1]] = {}
        person_information[show[1]]["years"] = show[2]
        person_information[show[1]]["born"] = show[3]
    main_string = input()

if person_information:
    for name in person_information:
        print(f"Name of the person: {name}")
        print(f"Age of the person: {person_information[name]['years']}.")
        print(f"Birthdate of the person: {person_information[name]['born']}")
else:
    print("DB is empty")
