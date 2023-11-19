city_name = input()
money = float(input())

cities = "Sofia, Varna, Plovdiv"

if money < 0:
    print("error")
if city_name not in cities:
    print("error")

if 0 <= money <= 500 and city_name == "Sofia":
    commisions = money * 0.05
    print(f"{commisions:.2f}")
elif 0 <= money <= 500 and city_name == "Varna":
    commisions = money * 0.045
    print(f"{commisions:.2f}")
elif 0 <= money <= 500 and city_name == "Plovdiv":
    commisions = money * 0.055
    print(f"{commisions:.2f}")


if 500 < money <= 1000 and city_name == "Sofia":
    commisions = money * 0.07
    print(f"{commisions:.2f}")
elif 500 < money <= 1000 and city_name == "Varna":
    commisions = money * 0.075
    print(f"{commisions:.2f}")
elif 500 < money <= 1000 and city_name == "Plovdiv":
    commisions = money * 0.08
    print(f"{commisions:.2f}")

if 1000 < money <= 10000 and city_name == "Sofia":
    commisions = money * 0.08
    print(f"{commisions:.2f}")
elif 1000 < money <= 10000 and city_name == "Varna":
    commisions = money * 0.10
    print(f"{commisions:.2f}")
elif 1000 < money <= 10000 and city_name == "Plovdiv":
    commisions = money * 0.12
    print(f"{commisions:.2f}")

if money > 10000 and city_name == "Sofia":
    commisions = money * 0.12
    print(f"{commisions:.2f}")
elif money > 10000 and city_name == "Varna":
    commisions = money * 0.13
    print(f"{commisions:.2f}")
elif money > 10000 and city_name == "Plovdiv":
    commisions = money * 0.145
    print(f"{commisions:.2f}")










