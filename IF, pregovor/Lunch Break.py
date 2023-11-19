import math

series_name = str(input())
episode_time = int(input())
rest_time = int(input())

lunch_time = 0.125 * rest_time
meditation_time = 0.25 * rest_time

time_for_series = rest_time - lunch_time - meditation_time
if episode_time <= time_for_series:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(time_for_series - episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(abs(time_for_series - episode_time))} more minutes.")

