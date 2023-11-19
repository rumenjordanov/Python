budget = float(input())
season = str(input())

destination = ""
type = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        cost = 0.30 * budget
        type = "Camp"
        print(f"Somewhere in {destination}")
        print(f"{type} - {cost:.2f}")
    elif season == "winter":
        cost = 0.70 * budget
        type = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{type} - {cost:.2f}")

if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        cost = 0.40 * budget
        type = "Camp"
        print(f"Somewhere in {destination}")
        print(f"{type} - {cost:.2f}")
    elif season == "winter":
        cost = 0.80 * budget
        type = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{type} - {cost:.2f}")

if budget > 1000:
    destination = "Europe"
    cost = 0.90 * budget
    type = "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{type} - {cost:.2f}")


