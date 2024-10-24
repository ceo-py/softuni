from collections import deque

strength_kick_the_ball = [int(x) for x in input().split()]
accuracy_direct_the_ball= deque(int(x) for x in input().split())
scored_goals = 0

while strength_kick_the_ball and  accuracy_direct_the_ball:

    strength = strength_kick_the_ball.pop()
    accuracy = accuracy_direct_the_ball.popleft()

    total_score = strength + accuracy

    if total_score == 100:
        scored_goals += 1

    if total_score > 100:
        strength -= 10
        strength_kick_the_ball.append(strength)
        accuracy_direct_the_ball.append(accuracy)

    elif total_score < 100:
        if strength < accuracy:
            accuracy_direct_the_ball.appendleft(accuracy)
        elif strength > accuracy:
            strength_kick_the_ball.append(strength)
        elif strength == accuracy:
            strength_kick_the_ball.append(total_score)

if scored_goals == 3:
    print("Paul scored a hat-trick!")
elif scored_goals == 0:
    print("Paul failed to score a single goal.")
elif scored_goals > 3:
    print("Paul performed remarkably well!")
elif scored_goals < 3:
    print("Paul failed to make a hat-trick.")

if scored_goals:
    print(f"Goals scored: {scored_goals}")

if strength_kick_the_ball:
    print(f"Strength values left: {', '.join([str(x) for x in strength_kick_the_ball])}")
if accuracy_direct_the_ball:
    print(f"Accuracy values left: {', '.join([str(x) for x in accuracy_direct_the_ball])}")