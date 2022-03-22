morse_code_msg = input().split(" | ")

morse_code_dic = {'..-.': 'F', '-..-': 'X',
                  '.--.': 'P', '-': 'T', '..---': '2',
                  '....-': '4', '-----': '0', '--...': '7',
                  '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                  '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                  '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                  '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                  '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                  '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}

show_result = ""

for letter in morse_code_msg:
    for ltr in letter.split(" "):
        if ltr != '':
            show_result += morse_code_dic[ltr]
    show_result += " "

print(show_result.upper())


# show_result = ""
#
# for letter in morse_code_msg:
#     find_letters = ""
#     for ltr in letter:
#         if ltr != " ":
#             find_letters += ltr
#         elif ltr == " " and find_letters != "":
#             show_result += morse_code_dic[find_letters]
#             find_letters = ""
#     if find_letters != "":
#         show_result += morse_code_dic[find_letters] + " "
# print(show_result.upper())