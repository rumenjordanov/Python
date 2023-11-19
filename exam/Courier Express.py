kg = float(input())
service = str(input())
km = int(input())
km_price = 0
nadcenka = 0
if service == "standard":
    if kg <= 1:
        km_price = 0.03
    elif 1 < kg < 10:
        km_price = 0.05
    elif 10 <= kg < 40:
        km_price = 0.10
    elif 40 <= kg < 90:
        km_price = 0.15
    elif 90 <= kg <= 150:
        km_price = 0.20
    price = km * km_price
    print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price:.2f} lv.")

if service == "express":
    if kg <= 1:
        km_price = 0.03
        nadcenka = 0.80
    elif 1 < kg < 10:
        km_price = 0.05
        nadcenka = 0.40
    elif 10 <= kg < 40:
        km_price = 0.10
        nadcenka = 0.05
    elif 40 <= kg < 90:
        km_price = 0.15
        nadcenka = 0.02
    elif 90 <= kg <= 150:
        km_price = 0.20
        nadcenka = 0.01

    transport = km * km_price
    nadcenka_kg = km_price * nadcenka
    nadcenka_km = kg * nadcenka_kg
    all_nadcenka = km * nadcenka_km
    price = transport + all_nadcenka

    print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price:.2f} lv.")





