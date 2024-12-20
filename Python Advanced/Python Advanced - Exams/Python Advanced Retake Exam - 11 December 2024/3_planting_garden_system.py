def plant_garden(available_space, *allowed_plants, **plant_requests):
    planted = {}
    allowed = {plant: space for plant, space in allowed_plants}

    for plant, qty in sorted(plant_requests.items()):
        if plant not in allowed:
            continue

        space = allowed[plant]
        possible = int(available_space / space)
        to_plant = min(possible, qty)

        if to_plant <= 0:
            continue

        planted[plant] = to_plant
        available_space -= to_plant * space

    success = planted == {p: q for p,
    q in plant_requests.items() if p in allowed}

    msg = f"All plants were planted! Available garden space: {available_space:.1f} sq meters." if success else "Not enough space to plant all requested plants!"
    result = [msg, "Planted plants:"]
    result.extend(f"{p}: {q}" for p, q in planted.items())

    return "\n".join(result)
