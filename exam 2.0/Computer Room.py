month = input()
hours = int(input())
people = int(input())
day_night = input()

if month == "march" or month == "april" or month == "may":
    if day_night == "day":
        price = 10.50
    else:
        price = 8.40
elif month == "june" or month == "july" or month == "august":
    if day_night == "day":
        price = 12.60
    else:
        price = 10.20

if people >= 4:
    price = price - price * 0.10

if hours >= 5:
    price = price - price * 0.50

all_price = price * people * hours

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {all_price:.2f}")
