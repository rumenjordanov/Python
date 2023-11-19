deposit_sum = float(input())
deposit_term = int(input())
procent = float(input())

sum = deposit_sum + deposit_term * ((deposit_sum * procent/100) / 12)

print(sum)
