string_ = input()

number_coffees = 0
events = ["coding", "dog", "cat", "movie"]
while string_ != "END":
    if string_.lower() in events:
        if string_ in events:
            number_coffees += 1
        else:
            number_coffees += 2
    string_ = input()

if number_coffees > 5:
    print("You need extra sleep")
else:
    print(number_coffees)






