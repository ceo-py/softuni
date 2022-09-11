from collections import deque

elfs_energy = deque(int(x) for x in input().split())
materials_in_box = [int(x) for x in input().split()]

info = {
    "toys": 0,
    "energy spend": 0,
    "counter": 0
}


def make_toys(energy, box, toys):
    elfs_energy.append(energy - (box - 1))
    info["toys"] += toys
    info["energy spend"] += box


def every_third_time(energy, box):
    make_toys(energy, box, 2)


def every_fifth_time(energy, box):
    elfs_energy.append(energy - box)
    info["energy spend"] += box


def not_enough_energy(energy, box):
    elfs_energy.append(energy * 2)
    materials_in_box.append(box)


def multiply_turns(energy, box, turn_time, adding_box=False):
    multiply_box = box
    if adding_box:
        multiply_box = box * 2
    if energy >= multiply_box:
        if turn_time == 5:
            every_fifth_time(energy, multiply_box)
        elif turn_time == 3:
            every_third_time(energy, multiply_box)
    else:
        not_enough_energy(energy, box)


while elfs_energy and materials_in_box:
    energy = elfs_energy.popleft()
    if energy < 5:
        continue

    info["counter"] += 1
    box = materials_in_box.pop()
    if info["counter"] % 3 == 0 and info["counter"] % 5 == 0:
        multiply_turns(energy, box, 5, True)
    elif info["counter"] % 3 == 0:
        multiply_turns(energy, box, 3, True)
    elif info["counter"] % 5 == 0:
        multiply_turns(energy, box, 5)
    elif box > energy:
        not_enough_energy(energy, box)
    else:
        make_toys(energy, box, 1)

print(f"Toys: {info['toys']}")
print(f"Energy: {info['energy spend']}")
if elfs_energy:
    print(f"Elves left: {', '.join(str(x) for x in elfs_energy)}")
if materials_in_box:
    print(f"Boxes left: {', '.join(str(x) for x in materials_in_box)}")






# from collections import deque
#
# energy = deque([int(i) for i in input().split()])
# materials = deque([int(i) for i in input().split()])
#
# toys = 0
# counter = 0
# energy_spent = 0
#
# while materials and energy:
#     while energy[0] < 5:
#         energy.popleft()
#         if len(energy) == 0:
#             break
#     if len(energy) == 0:
#         break
#     counter += 1
#     if counter % 3 != 0:
#         if energy[0] >= materials[-1]:
#             if counter % 5 == 0:
#                 energy[0] -= materials[-1]
#             else:
#                 energy[0] -= materials[-1] - 1
#                 toys += 1
#             energy_spent += materials[-1]
#             materials.pop()
#             energy.append(energy.popleft())
#         else:
#             energy[0] *= 2
#             energy.append(energy.popleft())
#     elif counter % 3 == 0:
#         if energy[0] >= materials[-1] * 2:
#             if counter % 5 == 0:
#                 energy[0] -= materials[-1] * 2
#             else:
#                 energy[0] -= materials[-1] * 2 - 1
#                 toys += 2
#             energy_spent += materials[-1] * 2
#             materials.pop()
#             energy.append(energy.popleft())
#         else:
#             energy[0] *= 2
#             energy.append(energy.popleft())
#
#
# print(f"Toys: {toys}")
# print(f"Energy: {energy_spent}")
# if (len(energy) > 0):
#     print(f"Elves left: {', '.join([str(i) for i in energy])}")
# if (len(materials) > 0):
#     print(f"Boxes left: {', '.join([str(i) for i in materials])}")