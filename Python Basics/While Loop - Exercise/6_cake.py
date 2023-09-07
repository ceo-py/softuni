cake_width = int(input())
cake_length = int(input())
cake_slices = input()

cake_size = cake_width * cake_length

while cake_slices != 'STOP':

    cake_slices = int(cake_slices)
    cake_size -= cake_slices

    if cake_size <= 0:
        print(f"No more cake left! You need {abs(cake_size)} pieces more.")
        break

    cake_slices = input()

else:
    print(f"{cake_size} pieces are left.")










# cake_width = int(input())
# cake_length = int(input())
#
# cake_size = cake_width * cake_length
# cake_slices_taken = 0
#
# while True:
#     cake_slices = input()
#
#     if cake_slices == "STOP":
#         cake_size -= cake_slices_taken
#         print(f"{cake_size} pieces are left.")
#         break
#
#     cake_slices_taken += int(cake_slices)
#     if cake_size < cake_slices_taken:
#         cake_slices_taken -= cake_size
#         print(f"No more cake left! You need {cake_slices_taken} pieces more.")
#         break
