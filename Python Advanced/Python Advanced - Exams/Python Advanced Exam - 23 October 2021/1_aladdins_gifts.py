from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gifts = {
    'Diamond Jewellery': {"quantity": 0, "min": 400, "max ": 499},
    'Gemstone': {"quantity": 0, "min": 100, "max ": 199},
    'Gold': {"quantity": 0, "min": 300, "max ": 399},
    'Porcelain Sculpture': {"quantity": 0, "min": 200, "max ": 299}
}


def under_100(material, magic_level):
    if total_sum % 2 == 0:
        return (material * 2) + (magic_level * 3)
    return (material + magic_level) * 2


while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()
    total_sum = material + magic_level
    if total_sum < 100:
        total_sum = under_100(material, magic_level)
    if total_sum > 499:
        total_sum /= 2
    for key, (_, min_, max_) in gifts.items():
        if gifts[key][min_] <= total_sum <= gifts[key][max_]:
            gifts[key]['quantity'] += 1
            break

if gifts['Gemstone']['quantity'] > 0 and gifts['Porcelain Sculpture']['quantity'] > 0 or \
        gifts['Gold']['quantity'] > 0 and gifts['Diamond Jewellery']['quantity'] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present, (quantity, _, __) in gifts.items():
    if gifts[present][quantity]:
        print(f"{present}: {gifts[present][quantity]}")










#
#
#
# from collections import deque
#
# materials = [int(x) for x in input().split()]
# magic_levels = deque(int(x) for x in input().split())
#
# gifts = {
#     'Diamond Jewellery': 0,
#     'Gemstone': 0,
#     'Gold': 0,
#     'Porcelain Sculpture': 0
# }
#
#
# def under_100(material, magic_level):
#     if total_sum % 2 == 0:
#         new_mix = (material * 2) + (magic_level * 3)
#     else:
#         new_mix = (material + magic_level) * 2
#     return new_mix
#
#
# while materials and magic_levels:
#     material = materials.pop()
#     magic_level = magic_levels.popleft()
#     total_sum = material + magic_level
#     if total_sum < 100:
#         total_sum = under_100(material, magic_level)
#     if total_sum > 499:
#         total_sum /= 2
#     if 100 <= total_sum <= 199:
#         gifts['Gemstone'] += 1
#     elif 200 <= total_sum <= 299:
#         gifts['Porcelain Sculpture'] += 1
#     elif 300 <= total_sum <= 399:
#         gifts['Gold'] += 1
#     elif 400 <= total_sum <= 499:
#         gifts['Diamond Jewellery'] += 1
#
#
# if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or \
#     gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0:
#     print("The wedding presents are made!")
# else:
#     print("Aladdin does not have enough wedding presents.")
#
# if materials:
#     print(f"Materials left: {', '.join(str(x) for x in materials)}")
#
# if magic_levels:
#     print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
#
# for present, quantity in gifts.items():
#     if quantity:
#         print(f"{present}: {quantity}")
#
#
#
#
#
#
#
#
#
#
#
#

