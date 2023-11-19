name = str(input())
next_class = 1
average = 0
fails = 0

while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails >= 2:
            print(f"{name} has been excluded at {next_class} grade")
            break
        continue
    next_class += 1
    average += grade
    if next_class > 12:
        print(f"{name} graduated. Average grade: {average / 12}")

