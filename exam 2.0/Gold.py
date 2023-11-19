locations = int(input())

for i in range(locations):
    expected_avg_gold_per_day = float(input())
    days = int(input())
    total_gold = 0

    for l in range(days):
        gold_per_day = float(input())
        total_gold = total_gold + gold_per_day

    avg_gold_per_day = total_gold / days

        if avg_gold_per_day >= expected_avg_gold_per_day:
            print(f'Good job! Average gold per day: {avg_gold_per_day:.2f}.')
        else:
            difference = expected_avg_gold_per_day - avg_gold_per_day
            print(f'You need {difference:.2f} gold.')