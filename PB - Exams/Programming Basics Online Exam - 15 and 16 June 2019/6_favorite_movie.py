movie_name = input()
best_movie_score, best_movie_name, movie_counter = 0, "", 0

while movie_name != "STOP":
    movie_counter += 1
    current_movie_score = 0
    for letter in movie_name:
        if letter.islower():
            current_movie_score = current_movie_score + ord(letter) - (len(movie_name) * 2)
        elif letter.isupper():
            current_movie_score = current_movie_score + ord(letter) - len(movie_name)
        else:
            current_movie_score = current_movie_score + ord(letter)
    if current_movie_score > best_movie_score:
        best_movie_name = movie_name
        best_movie_score = current_movie_score
    if movie_counter == 7:
        print(f"The limit is reached.\nThe best movie for you is {best_movie_name} with {best_movie_score} ASCII sum.")
        break
    movie_name = input()
else:
    print(f"The best movie for you is {best_movie_name} with {best_movie_score} ASCII sum.")












#
# import string
#
# current_movie_score = 0
# best_movie_score = 0
# best_movie_name = ""
# small_letter_count = 0
# big_letters_count = 0
# lower_letters = string.ascii_lowercase
# upper_letters = string.ascii_uppercase
# movie_counter = 0
#
# while True:
#     movie_counter += 1
#     movie_name = input()
#
#     if movie_name == "STOP":
#         print(f"The best movie for you is {best_movie_name} with {best_movie_score} ASCII sum.")
#         break
#
#     else:
#         for letter in movie_name:
#
#             if letter in lower_letters:
#                 small_letter_count += 1
#                 current_movie_score = current_movie_score + ord(letter) - (len(movie_name) * 2)
#
#             elif letter in upper_letters:
#                 big_letters_count += 1
#                 current_movie_score = current_movie_score + ord(letter) - len(movie_name)
#
#             else:
#                 current_movie_score = current_movie_score + ord(letter)
#
#     if current_movie_score > best_movie_score:
#         best_movie_name = movie_name
#         best_movie_score = current_movie_score
#
#     if movie_counter == 7:
#         print(f"The limit is reached.\nThe best movie for you is {best_movie_name} with {best_movie_score} ASCII sum.")
#         break
#
#     small_letter_count = 0
#     big_letters_count = 0
#     current_movie_score = 0
