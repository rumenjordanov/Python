from math import ceil

price_for_one_gpu = int(input())
price_for_one_prehodnik = int(input())
price_for_energy_one_day_one_gpu = float(input())
profit_one_day = float(input())

price_all_gpu = price_for_one_gpu * 13
price_all_prehodnici = price_for_one_prehodnik * 13

price_for_all = price_all_gpu + price_all_prehodnici + 1000
profit = profit_one_day - price_for_energy_one_day_one_gpu
all_profit_day = 13 * profit
days_for_profit = price_for_all / all_profit_day
print(price_for_all)
print(ceil(days_for_profit))