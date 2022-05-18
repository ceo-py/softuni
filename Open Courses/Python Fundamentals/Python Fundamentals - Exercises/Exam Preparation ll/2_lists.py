data_input = input()

while data_input != "stop playing":
    data_input = [int(x) for x in (" ".join(data_input.split())).split()]
    if len(set(data_input)) == len(data_input):
        result = [x + 2 if x % 2 == 0 else x for x in data_input]
        print(f"Unique list: {','.join([str(x) for x in sorted(result)])}")
        print(f"Output: {(sum(result) / len(result)):.2f}")
    else:
        result = [x + 3 if x % 2 != 0 else x for x in data_input]
        print(f"Non-unique list: {':'.join([str(x) for x in sorted(result)])}")
        print(f"Output: {(sum(result) / len(result)):.2f}")
    data_input = input()
