input_emojis = input()
happy_list = (":)", ":D", ";)", ":*", ":]", ";]", ":}", ";}", "(:", "*:", "c:", "[:", "[;")
sad_list = (":(", "D:", ";(", ":[", ";[", ":{", ";{", "):", ":c", "]:", "];")

happy_result = sum([input_emojis.count(emo) for emo in happy_list])
sad_result = sum([input_emojis.count(emo) for emo in sad_list])

happiness_index = happy_result / sad_result
if 2 < happiness_index or happiness_index == 2:
    face = ":D"
elif happiness_index > 1:
    face = ":)"
elif happiness_index == 1:
    face = ":|"
elif happiness_index < 1:
    face = ":("

print(f"Happiness index: {happiness_index:.2f} {face}")
print(f"[Happy count: {happy_result}, Sad count: {sad_result}]")
