name = input()
password = input()
check_password = input()
while check_password != password:
    check_password = input()
print(f"Welcome {name}!")

