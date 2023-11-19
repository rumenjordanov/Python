# Read User Input
n = int(input())
left_sum = 0
right_sum = 0

# Logic
for i in range(n):
    user_input = int(input())
    left_sum += user_input

for i in range(n):
    user_input = int(input())
    right_sum += user_input



# Output
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")

