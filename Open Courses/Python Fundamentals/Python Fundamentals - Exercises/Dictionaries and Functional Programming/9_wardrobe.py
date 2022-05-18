number_customers = int(input())

wardrobe_info = {}

for _ in range(number_customers):
    customer = input().split(" -> ")
    if customer[0] not in wardrobe_info:
        wardrobe_info[customer[0]] = {}
    for item in customer[1].split(","):
        if item not in wardrobe_info[customer[0]]:
            wardrobe_info[customer[0]][item] = 0
        wardrobe_info[customer[0]][item] += 1


def show_result(color, item):
    for col in wardrobe_info:
        print(f"{col} clothes:")
        for key, value in wardrobe_info[col].items():
            f_ = ""
            if col == color and key == item:
                f_ = "(found!)"
            print(f"* {key} - {value} {f_}")


check_for = input().split()
show_result(check_for[0], check_for[-1])
