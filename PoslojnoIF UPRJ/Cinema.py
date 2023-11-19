type = str(input())
r = int(input())
c = int(input())
income = 0

if type == "Premiere":
    income = r * c * 12
    print(f"{income:.2f} leva")
elif type == "Normal":
    income = r * c * 7.50
    print(f"{income:.2f}")
elif type == "Discount":
    income = r * c * 5.00
    print(f"{income:.2f}")
