broi_nailon = int(input())
litri_boq = int(input())
razreditel = int(input())
maistor_chasove = int(input())

dobavka_nailon = broi_nailon + 2
dobavka_boq = (litri_boq * 0.10) + litri_boq

cena_vsichko = dobavka_boq * 14.50 + dobavka_nailon * 1.50 + razreditel * 5 + 0.40


maistor_plashtane = (0.30 * cena_vsichko) * maistor_chasove

cena_s_maistora = cena_vsichko + maistor_plashtane

print(cena_s_maistora)
