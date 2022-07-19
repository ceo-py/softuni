import re

number_products_to_scan = int(input())
default_barcode = "00"
group_d = "Product group:"
patterns = re.compile(r"@[#]+(?P<found_text>[A-Z][a-zA-Z0-9]{4,}[A-Z])@[#]+")
for _ in range(number_products_to_scan):
    bar_code = input()
    main_string = re.finditer(patterns, bar_code)
    found = False
    for a in main_string:
        found = True
        result = "".join(x for x in a["found_text"] if x.isdigit())
        if result:
            print(f"{group_d} {result}")
        else:
            print(f"{group_d} {default_barcode}")
    if not found:
        print("Invalid barcode")










#
#
#
# import re
#
# number_barcodes = int(input())
# default_barcode = "00"
# for _ in range(number_barcodes):
#     bar_code = input()
#     patterns = re.compile(r"\@{1}[#]{1,}([A-Z]{1}[A-z0-9]{4,}[A-Z]{1})\@{1}[#]{1,}")
#     main_string = re.finditer(patterns, bar_code)
#     find_not_letter_or_number = False
#     there_is_print_already = False
#     for show in main_string:
#         there_si_number = False
#         barcode_show = ""
#         for letter in show[1]:
#             if letter.isalpha() or letter.isdigit():
#                 if letter.isdigit():
#                     barcode_show += str(letter)
#                     if not there_si_number:
#                         there_si_number = True
#             else:
#                 find_not_letter_or_number = True
#                 break
#         if not find_not_letter_or_number and not there_si_number:
#             print(f"Product group: {default_barcode}")
#             there_is_print_already = True
#         elif there_si_number:
#             print(f"Product group: {barcode_show}")
#             there_is_print_already = True
#     if not there_is_print_already:
#         print("Invalid barcode")
