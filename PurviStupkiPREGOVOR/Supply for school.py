count_pen = int(input())
count_markers = int(input())
litri_preparat = int(input())
namalenie = int(input())

cena_himikalni = count_pen * 5.80
cena_markers = count_markers * 7.20
cena_preparat = litri_preparat * 1.20

cena_vsichki = cena_himikalni + cena_markers + cena_preparat

finalna_cena = cena_vsichki * ( namalenie / 100)

oficialno_namalenie = cena_vsichki - finalna_cena

print(oficialno_namalenie)
