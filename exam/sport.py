height = 5364
days = 1
while True:
    sleep = str(input())
    if sleep == "Yes":
        days += 1
    elif sleep == "No":
        days += 0
    climbed = int(input())
    height += climbed
    if height >= 8848:
        print(f"Goal reached for {days} days!")
        break
    elif days >= 5 or sleep == "END":
        print("Failed!")
        print(height)
        break
