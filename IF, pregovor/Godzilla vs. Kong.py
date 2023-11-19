max_film_price = float(input())
walking_men = int(input())
money_for_one_walking_men_clothing = float(input())

decor = max_film_price * 0.10


if walking_men > 150:
    money_for_one_walking_men_clothing = money_for_one_walking_men_clothing - money_for_one_walking_men_clothing * 0.10

statists = walking_men * money_for_one_walking_men_clothing
total_sum = decor + statists
film_price = abs(max_film_price - total_sum)

if max_film_price - total_sum >= 0:
    print(f"Action!")
    print(f"Wingard starts filming with {film_price:.2f} leva left.")

else:
    print(f"Not enough money!")
    print(f"Wingard needs {film_price:.2f} leva more.")


