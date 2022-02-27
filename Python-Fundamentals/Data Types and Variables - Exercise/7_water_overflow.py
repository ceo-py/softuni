number_of_pipes = int(input())

capacity = 255
total_capacity_left = 0

for _ in range(number_of_pipes):

    pipe = int(input())

    if capacity - pipe >= 0:
        capacity += - pipe
        total_capacity_left += pipe

    else:
        print("Insufficient capacity!")

print(total_capacity_left)
