broi_pileta = int(input())
broi_riba = int(input())
broi_vegan = int(input())

cena_bez_desert = broi_pileta * 10.35 + broi_riba * 12.40 + broi_vegan * 8.15

cena_na_desert = cena_bez_desert * 0.20

obsta_cena = cena_bez_desert + cena_na_desert + 2.50

print(obsta_cena)
