print("Kolko struvashe zubolekarqt?")
dentist = int(input())
print("Kolko pari izharchi dnes v qdene")
food_tuesday = int(input())
print("Kolko struvashe trenirovkata?")
training = int(input())


Rumen_money = 80
given_money = 200

money_used = dentist + food_tuesday + training
money_in_the_end = Rumen_money + given_money - money_used

if money_in_the_end <= 80:
    print(f"Nikolay must give  {80 - money_in_the_end} to Rumen")
else:
    print(f"Rumen must give {money_in_the_end - 80} to Nikolay")


