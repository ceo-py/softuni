game_moves = int(input())

total_score = 0
from_zero_to_nine = 0
from_ten_to_nineteen = 0
from_twenty_to_twenty_nine = 0
from_forty_to_fifty = 0
from_thirty_to_thirty_nine = 0
invalid_number = 0

for _ in range(1, game_moves + 1):
    number = int(input())

    if 0 > number or number > 50:
        invalid_number += 1
        total_score = total_score / 2

    elif number < 10:
        from_zero_to_nine += 1
        total_score += + (number * 0.20)

    elif number < 20:
        from_ten_to_nineteen += 1
        total_score += + (number * 0.30)

    elif number < 30:
        from_twenty_to_twenty_nine += 1
        total_score += + (number * 0.40)

    elif number < 40:
        from_thirty_to_thirty_nine += 1
        total_score += + 50

    elif number <= 50:
        from_forty_to_fifty += 1
        total_score += + 100

from_zero_to_nine = (from_zero_to_nine / game_moves) * 100
from_ten_to_nineteen = (from_ten_to_nineteen / game_moves) * 100
from_twenty_to_twenty_nine = (from_twenty_to_twenty_nine / game_moves) * 100
from_thirty_to_thirty_nine = (from_thirty_to_thirty_nine / game_moves) * 100
from_forty_to_fifty = (from_forty_to_fifty / game_moves) * 100
invalid_number = (invalid_number / game_moves) * 100

print(f"{total_score:.2f}")
print(f"From 0 to 9: {from_zero_to_nine:.2f}%")
print(f"From 10 to 19: {from_ten_to_nineteen:.2f}%")
print(f"From 20 to 29: {from_twenty_to_twenty_nine:.2f}%")
print(f"From 30 to 39: {from_thirty_to_thirty_nine:.2f}%")
print(f"From 40 to 50: {from_forty_to_fifty:.2f}%")
print(f"Invalid numbers: {invalid_number:.2f}%")
