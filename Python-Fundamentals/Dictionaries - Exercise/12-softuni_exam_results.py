command = input()

examp_results = {}
total_people_show = {}


def ban_remove(name):
    for lang_name in examp_results:
        for key, value in examp_results[lang_name].items():
            if key == name:
                examp_results[lang_name].pop(key)
                break


def adding_scores(name, lang, score):
    if lang not in examp_results:
        examp_results[lang] = {}
        total_people_show[lang] = {}
        total_people_show[lang][lang] = 0
    if name not in examp_results[lang]:
        examp_results[lang][name] = score
        total_people_show[lang][lang] += 1
    else:
        if examp_results[lang][name] < score:
            examp_results[lang][name] = score
        total_people_show[lang][lang] += 1


def show_result():
    print("Results:")
    for lang_name in examp_results:
        for name, score in examp_results[lang_name].items():
            print(f"{name} | {score}")
    print("Submissions:")
    for lang_name in total_people_show:
        for name, score in total_people_show[lang_name].items():
            print(f"{lang_name} - {score}")


while command != "exam finished":
    command = command.split("-")
    name = command[0]
    lang_name = command[1]
    if lang_name != "banned":
        score = command[-1]
        adding_scores(name, lang_name, score)
    else:
        ban_remove(name)

    command = input()

show_result()
