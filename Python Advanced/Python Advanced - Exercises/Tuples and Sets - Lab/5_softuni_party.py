number_of_guests = int(input())

reservation = {input() for _ in range(number_of_guests)}
guests_who_came = input()

while guests_who_came != "END":
    reservation.remove(guests_who_came)
    guests_who_came = input()

print(len(reservation))
print("\n".join(sorted(reservation)))












#
#
#
# number_of_guests = int(input())
#
# reservation = [input() for _ in range(number_of_guests)]
# guests_who_came = input()
# while guests_who_came != "END":
#     if guests_who_came in reservation:
#         reservation.remove(guests_who_came)
#     guests_who_came = input()
#
# print(len(reservation))
# vip, regular = [], []
# [vip.append(res) if res[0].isdigit() else regular.append(res) for res in reservation]
# if vip:
#     print('\n'.join(sorted(vip)))
# if regular:
#     print('\n'.join(sorted(regular)))