# Read User Input
n = int(input())
odd_sum = 0
even_sum = 0
# Logic
for i in range(n):
    user_input = int(input())
    if i % 2 == 0:
        odd_sum += user_input
    else:
        even_sum += user_input

if odd_sum == even_sum:
    print(f"Yes")
    print(f"Sum = {odd_sum}")
else:
    diff = abs(odd_sum - even_sum)
    print(f"No")
    print(f"Diff = {diff}")
