product = str(input())
city = str(input())
quantity = float(input())


if city == "Sofia":
    if product == "coffee":
        result = quantity * 0.50
    elif product == "water":
        result = quantity * 0.80
    elif product == "beer":
        result = quantity * 1.20
    elif product == "sweets":
        result = quantity * 1.45
    elif product == "peanuts":
        result = quantity * 1.60

if city == "Plovdiv":
    if product == "coffee":
        result = quantity * 0.40
    elif product == "water":
        result = quantity * 0.70
    elif product == "beer":
        result = quantity * 1.15
    elif product == "sweets":
        result = quantity * 1.30
    elif product == "peanuts":
        result = quantity * 1.50

if city == "Varna":
    if product == "coffee":
        result = quantity * 0.45
    elif product == "water":
        result = quantity * 0.70
    elif product == "beer":
        result = quantity * 1.10
    elif product == "sweets":
        result = quantity * 1.35
    elif product == "peanuts":
        result = quantity * 1.55


print(result)
