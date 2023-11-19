import math

record_seconds = float(input())
meters_distance = float(input())
time_for_one_meter = float(input())


need_to_swin = meters_distance * time_for_one_meter

resistent = math.floor(meters_distance / 15) * 12.5

all_time = need_to_swin + resistent

if all_time < record_seconds:
    print(f" Yes, he succeeded! The new world record is {all_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {all_time - record_seconds:.2f} seconds slower.")