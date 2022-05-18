list_input_ = input()

while list_input_ != "stop playing":
    list_input_ = (' '.join(list_input_.split())).split()
    if len(set(list_input_)) == len(list_input_):
        result_ = sorted([int(x) + 2 if int(x) % 2 == 0 else int(x) for x in list_input_])
        print(f"Unique list:", ','.join([str(x) for x in result_]))
        print(f"Output: {(sum(result_) / len(result_)):.2f}")
    else:
        result_ = sorted([int(x) + 3 if int(x) % 2 != 0 else int(x) for x in list_input_])
        print(f"Non-unique list:", ":".join([str(x) for x in result_]))
        print(f"Output: {(sum(result_) / len(result_)):.2f}")
    list_input_ = input()
