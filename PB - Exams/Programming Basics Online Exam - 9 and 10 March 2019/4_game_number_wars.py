player_one = input()
player_two = input()

player_one_score = 0
player_two_score = 0

player_one_card = input()

while player_one_card != "End of game":
    player_one_card = int(player_one_card)
    player_two_card = int(input())

    difference_score = abs(player_one_card - player_two_card)

    if difference_score == 0:
        player_one_card = int(input())
        player_two_card = int(input())
        winner = ""
        winner_points = 0

        if player_one_card > player_two_card:
            winner = player_one
            winner_points = player_one_score + difference_score

        elif player_one_card < player_two_card:
            winner = player_two
            winner_points = player_two_score + difference_score

        print("Number wars!")
        print(f"{winner} is winner with {winner_points} points")
        break

    if player_one_card > player_two_card:
        player_one_score += difference_score

    elif player_one_card < player_two_card:
        player_two_score += difference_score

    player_one_card = input()

else:
    print(f"{player_one} has {player_one_score} points")
    print(f"{player_two} has {player_two_score} points")










# player_one = input()
# player_two = input()
#
# player_one_score = 0
# player_two_score = 0
#
# while True:
#
#     card_player_one = input()
#
#     if card_player_one == "End of game":
#         print(f"{player_one} has {player_one_score} points\n{player_two} has {player_two_score} points")
#         break
#
#     else:
#         card_player_one = int(card_player_one)
#
#     card_player_two = int(input())
#
#     if card_player_one > card_player_two:
#         player_one_score += card_player_one - card_player_two
#
#     elif card_player_two > card_player_one:
#         player_two_score += card_player_two - card_player_one
#
#     elif card_player_two == card_player_one:
#         card_player_one = int(input())
#         card_player_two = int(input())
#
#         if card_player_one > card_player_two:
#             print(f"Number wars!\n{player_one} is winner with {player_one_score} points")
#             break
#
#         else:
#             print(f"Number wars!\n{player_two} is winner with {player_two_score} points")
#             break