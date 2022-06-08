number_of_user_names = int(input())
names = [input() for _ in range(number_of_user_names)]
print("\n".join(set(names)))