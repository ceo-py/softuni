player_one = input()
player_two = input()

player_one_score = 0
player_two_score = 0

while True:

    card_player_one = input()

    if card_player_one == "End of game":
        print(f"{player_one} has {player_one_score} points\n{player_two} has {player_two_score} points")
        break

    else:
        card_player_one = int(card_player_one)

    card_player_two = int(input())

    if card_player_one > card_player_two:
        player_one_score += card_player_one - card_player_two

    elif card_player_two > card_player_one:
        player_two_score += card_player_two - card_player_one

    elif card_player_two == card_player_one:
        card_player_one = int(input())
        card_player_two = int(input())

        if card_player_one > card_player_two:
            print(f"Number wars!\n{player_one} is winner with {player_one_score} points")
            break

        else:
            print(f"Number wars!\n{player_two} is winner with {player_two_score} points")
            break