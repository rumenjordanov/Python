age = float(input())
sex = str(input())

if sex == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")
if sex == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
