actor_name = input()
points_from_academy = float(input())
judges_number = int(input())

judges_score = points_from_academy
nominated = False

for judge in range(0, judges_number):
    judge_name = input()
    judge_points = float(input())
    judges_score += (len(judge_name) * (judge_points / 2))
    if judges_score > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {judges_score:.1f}!")
        nominated = True
        break

if nominated == False:
    judges_score = 1250.5 - judges_score
    print(f"Sorry, {actor_name} you need {judges_score:.1f} more!")
