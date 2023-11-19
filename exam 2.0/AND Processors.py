from math import floor
planed_cpu = int(input())
workers = int(input())
working_days = int(input())

all_working_hours_by_workers = workers * working_days * 8
all_working_hours_by_workers = floor(all_working_hours_by_workers / 3)

if all_working_hours_by_workers < planed_cpu:
    lower_than_planned = planed_cpu - all_working_hours_by_workers
    print(f"Losses: -> {lower_than_planned * 110.10:.2f} BGN")
else:
    more_than_planned = all_working_hours_by_workers - planed_cpu

    print(f"Profit: -> {more_than_planned * 110.10:.2f} BGN")
