def list_roman_emperors(*emperors, **emperors_dict):
    output = []
    successful_emperors = {}
    unsuccessful_emperors = {}

    for emperor_name, emperor_success in emperors:
        if emperor_success:
            successful_emperors[emperor_name] = 0
        else:
            unsuccessful_emperors[emperor_name] = 0

    for emperor_name, length in emperors_dict.items():
        if emperor_name in successful_emperors:
            successful_emperors[emperor_name] = length
        else:
            unsuccessful_emperors[emperor_name] = length

    output.append(
        f"Total number of emperors: {len(successful_emperors) + len(unsuccessful_emperors)}")

    if successful_emperors:
        output.append("Successful emperors:")
        output += [f"****{emperor_name}: {length}" for emperor_name, length in sorted(successful_emperors.items(), key=lambda x: (-x[1], x[0]))]
    if unsuccessful_emperors:
        output.append("Unsuccessful emperors:")
        output += [f"****{emperor_name}: {length}" for emperor_name, length in sorted(unsuccessful_emperors.items(), key=lambda x: (x[1], x[0]))]

    return "\n".join(output)

