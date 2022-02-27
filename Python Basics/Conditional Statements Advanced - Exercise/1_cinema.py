type_screen_play = input()
number_rows = int(input())
number_columns = int(input())

screen_type = {
    "Premiere": 12.00,
    "Normal": 7.50,
    "Discount": 5.00
}
capacity = number_rows * number_columns
total = screen_type[type_screen_play] * capacity
print(f"{total:.2f} leva")
