#Input
sales_all = 0
rate_all = 0
n = int(input())

#Logic
for i in range(n):
  number = int(input())
  sales = number // 10
  rate = number % 10

  if rate == 2:
    sales = 0
  elif rate == 3:
    sales = sales / 2
  elif rate == 4:
    sales = 0.7 * sales
  elif rate == 5:
    sales = 0.85 * sales

  sales_all += sales
  rate_all += rate
average_rate = rate_all / n
#Print
print(f'{sales_all:.2f}')
print(f'{average_rate:.2f}')