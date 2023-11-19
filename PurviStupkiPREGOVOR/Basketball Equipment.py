godishna_taksa = int(input())

kecove = godishna_taksa - godishna_taksa * 0.40
ekip = kecove - kecove * 0.20
topka = ekip * 0.25
aksesoari = topka * 0.20

vsichko = godishna_taksa + kecove + ekip + topka + aksesoari

print(vsichko)
