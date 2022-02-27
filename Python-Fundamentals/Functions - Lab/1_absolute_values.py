main_list = [float(n) for n in input().split()]

def abs_value(list):
    result = [abs(ele) for ele in main_list]
    return print(result)

abs_value(main_list)