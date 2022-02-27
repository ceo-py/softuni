client_number = int(input())

to_stop = 100

shop_info = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7
}

total_price = 0
items_buy = 0

for _ in range(0, client_number):
    customer_purchased = 0
    customer_items = 0
    for _ in range(0, to_stop):
        name_of_the_product = input()

        if name_of_the_product == "Finish":
            if customer_items % 2 == 0:
                customer_purchased = customer_purchased - (customer_purchased * 0.20)
                total_price += customer_purchased

            else:
                total_price += customer_purchased

            print(f"You purchased {customer_items} items for {customer_purchased:.2f} leva.")
            break

        else:
            customer_purchased += shop_info[name_of_the_product]
            items_buy += 1
            customer_items += 1

average_bill = total_price / client_number
print(f"Average bill per client is: {average_bill:.2f} leva.")
