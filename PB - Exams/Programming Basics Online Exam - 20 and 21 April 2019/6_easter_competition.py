easter_cake_number = int(input())

to_stop = 100
best_score = 0
best_baker = ""

for _ in range(0, easter_cake_number):
    baker_name = input()
    score = 0

    for _ in range(0, to_stop):
        score_number = input()

        if score_number == "Stop":
            if score > best_score:
                best_score = score
                best_baker = baker_name
                print(f"{baker_name} has {score} points.")
                print(f"{baker_name} is the new number 1!")
                break

            else:
                print(f"{baker_name} has {score} points.")
            break

        else:
            score += int(score_number)

print(f"{best_baker} won competition with {best_score} points!")
