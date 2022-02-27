time_for_pictures = int(input())
number_scenes = int(input())
time_for_a_scenes = int(input())

prepering_terrain = time_for_pictures * 0.15
time_take_to_shoot_the_scenes = number_scenes * time_for_a_scenes
time_needed = time_take_to_shoot_the_scenes + prepering_terrain

time_left = abs(time_for_pictures - time_needed)

if time_for_pictures <= time_needed:
    print(f"Time is up! To complete the movie you need {round(time_left)} minutes.")

else:
    print(f"You managed to finish the movie on time! You have {round(time_left)} minutes left!")
