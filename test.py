from random import randint

beetle_body = {
    "head": {"head": '''                     
                 ^       
              (     )''',
             "eyes": '''                     
               o ^ o     
              (     )''',
             "antennas": '''              \     /
          \      ^      /
            \ (     ) /''',
             "full head": '''              \     /
          \    o ^ o    /
            \ (     ) /'''
             },
    "body": {"body":
             '''             (%%%%%%%) 
             )%%%%%%%(   

             (%%%%%%%)          
             (%%%%%%%)  
             (       ) 
              (%%%%%)    
               (%%%)
                 !''',
             "legs":
             '''             (%%%%%%%) 
             )%%%%%%%(   

             (%%%%%%%)          
             (%%%%%%%)  
            /(       )\\
          /   (%%%%%)   \\
               (%%%)
                 !''',
             "wings":
 ''' ____________(%%%%%%%)____________
(     /   /  )%%%%%%%(  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(%%%%%%%)\  \     )
    (__/___/ (%%%%%%%) \___\__)
             (       )  
              (%%%%%)     
               (%%%)
                 !''',
             "full body":
 ''' ____________(%%%%%%%)____________
(     /   /  )%%%%%%%(  \   \     )
(___/___/__/           \__\___\___)
   (     /  /(%%%%%%%)\  \     )
    (__/___/ (%%%%%%%) \___\__)
            /(       )\\
          /   (%%%%%)   \\
               (%%%)
                 !'''}
}

print(beetle_body["head"]["full head"])
print(beetle_body["body"]["full body"])


player_info = {
    "body": [1, False],
    "head": [2, False],
    "legs": [3, False],
    "eyes": [4, False],
    "antenna": [5, False],
    "wings": [6, False]
}
computer_info = {
    "body": [1, False],
    "head": [2, False],
    "legs": [3, False],
    "eyes": [4, False],
    "antenna": [5, False],
    "wings": [6, False]
}


def roll_dice():
    return randint(1, 6)


def logic_body(player_or_cpu_):
    if not player_or_cpu_["body"][1]:
        print(beetle_body["body"]["body"])
        player_or_cpu_["body"][1] = True
    else:
        print("You Already have that part body!")


def head_logic(player_or_cpu_):
    if player_or_cpu_["body"][1]:
        if not player_or_cpu_["head"][1]:
            print(beetle_body["head"]["head"])
            print(beetle_body["body"]["body"])
            player_or_cpu_["head"][1] = True
        else:
            print("You Already have that part head!")
    else:
        print("You still don't have body part!")

def eye_logic(player_or_cpu_):
    if player_or_cpu_["head"][1]:
        if not player_or_cpu_["eyes"][1]:
            print(beetle_body["head"]["eyes"])
            if all([player_or_cpu_["legs"], player_or_cpu_["wings"]]):
                print(beetle_body["body"]["full body"])
            elif player_or_cpu_["legs"]:
                print(beetle_body["body"]["legs"])
            elif player_or_cpu_["wings"]:
                print(beetle_body["body"]["legs"])
            else:
                print(beetle_body["body"]["body"])

            player_or_cpu_["head"][1] = True
        else:
            print("You Already have that part head!")
    else:
        print("You still don't have body part!")



player_one_name = input("What is your name? : ")
player_win = False
computer_win = False
player_or_cpu = 0  # even numbers player odd number cpu

while not player_win and not computer_win:
    dice = roll_dice()
    print(f"\n\n")
    if player_or_cpu % 2 == 0:
        print(f"{player_one_name} turn he roll the dice - {dice}")
        if dice == 1:
            logic_body(player_info)
        elif dice == 2:
            head_logic(player_info)
        print(f"{player_one_name} parts find:")
        for key, value in player_info.items():
            if value[1]:
                print(f"1/1 of {key}")
            else:
                print(f"0/1 of {key}")
    else:
        print(f"Computer turn he roll the dice - {dice}")
        if dice == 1:
            logic_body(computer_info)
        elif dice == 2:
            head_logic(computer_info)
        print("Computer parts find:")
        for key, value in computer_info.items():
            if value[1]:
                print(f"1/1 of {key}")
            else:
                print(f"0/1 of {key}")
    player_or_cpu += 1

# print(beetle_body["head"]["full head"], end="")
# print(beetle_body["body"]["full body"])
# print(beetle_body["head"])
