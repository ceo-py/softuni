volume_pool = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

pipe1_bring = pipe1 * hours
pipe2_bring = pipe2 * hours
filled_litters = pipe1_bring + pipe2_bring

pipe1_filled_percent = (pipe1_bring / filled_litters) * 100
pipe2_filled_percent = (pipe2_bring / filled_litters) * 100


filled_percent = (filled_litters / volume_pool) * 100



if filled_litters <= volume_pool:
    print(
        f'The pool is {filled_percent:.2f}% full. Pipe 1: {pipe1_filled_percent:.2f}%. Pipe 2: {pipe2_filled_percent:.2f}%.')
else:
    over_litters = abs(filled_litters - volume_pool)
    print(f"For {hours:.2f} hours the pool overflows with {over_litters:.2f} liters.")






# volume_pool_liters = int(input())
# pipe_one_debit_per_hour = int(input())
# pipe_two_debit_per_hour = int(input())
# hours_workers_missing = float(input())
#
# pipe_one_debit_total = hours_workers_missing * pipe_one_debit_per_hour
# pipe_two_debit_total = hours_workers_missing * pipe_two_debit_per_hour
#
# pool_total_filled = (pipe_one_debit_total + pipe_two_debit_total)
# pipe_one_filled_total = (pipe_one_debit_total / pool_total_filled) * 100
# pipe_two_filled_total = (pipe_two_debit_total / pool_total_filled) * 100
#
# pool_pipe_total = (pool_total_filled / volume_pool_liters) * 100
# if pool_total_filled <= volume_pool_liters:
#     print(f"The pool is {pool_pipe_total:.2f}% full. Pipe 1: {pipe_one_filled_total:.2f}%. "
#           f"Pipe 2: {pipe_two_filled_total:.2f}%.")
# else:
#     over_flows = abs(pool_total_filled - volume_pool_liters)
#     print(f"For {hours_workers_missing:.2f} hours the pool overflows with {over_flows:.2f} liters.")




# v = int(input())
# p1 = int(input())
# p2 = int(input())
# h = float(input())
#
# sum_p1 = p1 * h
# sum_p2 = p2 * h
# sum = sum_p1 + sum_p2
#
# percent_full = (sum / v) * 100
# first_p1_percent = (sum_p1 / sum) * 100
# second_p2_percent = (sum_p2 / sum) * 100
#
# if sum <= v:
#
#     print(f"The pool is {percent_full:.2f}% full. Pipe 1: {first_p1_percent:.2f}%. Pipe 2: {second_p2_percent:.2f}%.")
# else:
#     overflows = abs(sum - v)
#     print(f"For {h:.2f} hours the pool overlows with {overflows:.2f} liters.")
#
#



#
# volume_pool = int(input())
# pipe1 = int(input())
# pipe2 = int(input())
# hours = float(input())
#
# pipe1_bring = pipe1 * hours
# pipe2_bring = pipe2 * hours
# filled_litters = pipe1_bring + pipe2_bring
#
# pipe1_filled_percent = (pipe1_bring / filled_litters) * 100
# pipe2_filled_percent = (pipe2_bring / filled_litters) * 100
#
#
# filled_percent = (filled_litters / volume_pool) * 100
#
#
#
# if filled_litters <= volume_pool:
#     print(
#         f'The pool is {filled_percent:.2f}% full. Pipe 1: {pipe1_filled_percent:.2f}%. Pipe 2: {pipe2_filled_percent:.2f}%.')
# else:
#     over_litters = abs(filled_litters - volume_pool)
#     print(f"For {hours:.2} hours the pool overflows with {over_litters:.2f} liters.")
#
#
#
