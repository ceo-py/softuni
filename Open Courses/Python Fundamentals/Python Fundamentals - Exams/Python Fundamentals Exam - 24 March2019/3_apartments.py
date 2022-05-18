neighborhood = {}

adding_apartment = input()
while adding_apartment != "collectApartments":
    adding_apartment, blocks = adding_apartment.split(" -> ")
    if adding_apartment not in neighborhood:
        neighborhood[adding_apartment] = {}
    for x in blocks.split(","):
        neighborhood[adding_apartment][int(x)] = {}
    adding_apartment = input()

listing_check = input()
while listing_check != "report":
    neighbor, other = listing_check.split("&")
    block_number, app_info = other.split(" -> ")
    number_apartments, price = app_info.split("|")
    if neighbor in neighborhood:
        block_number = int(block_number)
        if block_number in neighborhood[neighbor]:
            del neighborhood[neighbor][block_number]
            neighborhood[neighbor][block_number] = {}
            neighborhood[neighbor][block_number][number_apartments] = price
    listing_check = input()


def show_result():
    for name in sorted(neighborhood):
        print(f"Neighborhood: {name}")
        for blocks in sorted(neighborhood[name]):
            if neighborhood[name][blocks]:
                for key, value in neighborhood[name][blocks].items():
                    print(f"* Block number: {blocks} -> {key} apartments for sale. Price for one: {value}")
            else:
                print(f"* Block number: {blocks} -> 0 apartments for sale. Price for one: None")


show_result()
