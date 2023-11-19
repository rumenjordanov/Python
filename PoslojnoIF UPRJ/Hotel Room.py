month = input()
nights = int(input())
studio = 0
apartment = 0
promotion = 0
final_price_apartment = 0
final_price_studio = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if nights <= 7:
        final_price_studio = studio * nights
        final_price_apartment = apartment * nights
    elif 7 < nights <= 14:
        all_for_studio = studio * nights
        promotion = 0.05 * all_for_studio
        final_price_studio = all_for_studio - promotion
        final_price_apartment = apartment * nights
    elif nights > 14:
        all_for_studio = studio * nights
        all_for_apartment = apartment * nights
        promotion = 0.30 * all_for_studio
        promotion_2 = 0.10 * all_for_apartment
        final_price_studio = all_for_studio - promotion
        final_price_apartment = all_for_apartment - promotion_2

if month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights <= 14:
        all_for_studio = studio * nights
        final_price_studio = all_for_studio
        final_price_apartment = apartment * nights
    elif nights > 14:
        all_for_studio = studio * nights
        all_for_apartment = apartment * nights
        promotion = 0.20 * all_for_studio
        promotion_2 = 0.10 * all_for_apartment
        final_price_studio = all_for_studio - promotion
        final_price_apartment = all_for_apartment - promotion_2
if month == "July" or month == "August":
    studio = 76
    apartment = 77
    if nights <= 14:
        all_for_studio = studio * nights
        final_price_studio = all_for_studio
        final_price_apartment = apartment * nights
    elif nights > 14:
        all_for_studio = studio * nights
        all_for_apartment = apartment * nights
        promotion_2 = 0.10 * all_for_apartment
        final_price_studio = all_for_studio
        final_price_apartment = all_for_apartment - promotion_2


print(f"Apartment: {final_price_apartment:.2f} lv.")
print(f"Studio: {final_price_studio:.2f} lv.")





