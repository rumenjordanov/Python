budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = gpu_count * 250
cpu_price = 0.35 * gpu_price
ram_price = 0.10 * gpu_price

all_price = gpu_price + (cpu_count * cpu_price) + (ram_count *ram_price)


if gpu_count > cpu_count:
    all_price = all_price - all_price * 0.15



if budget >= all_price:
    print(f"You have {budget - all_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {all_price - budget:.2f} leva more!")
