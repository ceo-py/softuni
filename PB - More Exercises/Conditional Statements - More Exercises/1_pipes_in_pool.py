volume_pool_liters = int(input())
pipe_one_debit_per_hour = int(input())
pipe_two_debit_per_hour = int(input())
hours_workers_missing = float(input())

pipe_one_debit_total = hours_workers_missing * pipe_one_debit_per_hour
pipe_two_debit_total = hours_workers_missing * pipe_two_debit_per_hour

pool_total_filled = (pipe_one_debit_total + pipe_two_debit_total)
pipe_one_filled_total = (pipe_one_debit_total / pool_total_filled) * 100
pipe_two_filled_total = (pipe_two_debit_total / pool_total_filled) * 100

pool_pipe_total = (pool_total_filled / volume_pool_liters) * 100
if pool_total_filled <= volume_pool_liters:
    print(f"The pool is {pool_pipe_total:.2f}% full. Pipe 1: {pipe_one_filled_total:.2f}%. "
          f"Pipe 2: {pipe_two_filled_total:.2f}%.")
else:
    over_flows = abs(pool_total_filled - volume_pool_liters)
    print(f"For {hours_workers_missing:.2f} hours the pool overflows with {over_flows:.2f} liters.")
