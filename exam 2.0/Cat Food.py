cats_number = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
total_food_weight = 0

for i in range(cats_number):
  food_weight = float(input())
  total_food_weight += food_weight
  if 100 <= food_weight < 200:
    group_1 += 1
  elif 200 <= food_weight < 300:
    group_2 += 1
  elif 300 <= food_weight <= 400:
    group_3 += 1

kg = total_food_weight / 1000
price = round(kg * 12.45, 2)

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {price:.2f} lv.")