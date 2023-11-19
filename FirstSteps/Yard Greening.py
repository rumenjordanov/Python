kv_metri = float(input())
bez_otstupka = kv_metri * 7.61
s_otstupka = bez_otstupka * 0.18
kolko_otstupka = bez_otstupka - s_otstupka

print(f"The final price is: {s_otstupka} lv.")
print(f"The discount is: {kolko_otstupka} lv.")