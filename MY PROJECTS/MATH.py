# INPUT
print("What is your math problem")
user_input = input()

# LOGIC


if user_input == "Sum":
    total = 0
    print("How many numbers?")
    n = int(input())
    print(f"Which {n} numbers?")
    for i in range(n):
        user_input = int(input())
        total += user_input
    print(f"Answer {total}")

elif user_input == "Table 1":
    for x in range(1,11):
        for y in range(1, 11):
          product = x * y
          print(f"{x} * {y} = {product}")



else:
    count = 0
    while True:
        print("Next update soon...")
        count += 1
        if count == 4:
            break