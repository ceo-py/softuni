number_of_names = int(input())

names = [input() for _ in range(number_of_names)]
print("\n".join(set(names)))