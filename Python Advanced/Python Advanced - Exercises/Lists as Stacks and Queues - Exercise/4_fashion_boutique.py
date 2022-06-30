clothes_in_box = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack = rack_capacity
used_racks = 1
while clothes_in_box:
    cloth_size = clothes_in_box.pop()
    if cloth_size <= current_rack:
        current_rack -= cloth_size
    else:
        used_racks += 1
        current_rack = rack_capacity
        current_rack -= cloth_size

print(used_racks)






