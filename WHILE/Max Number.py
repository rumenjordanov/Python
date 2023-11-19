
max_number = int(input())
while True:
    user_input = input()
    if user_input == 'Stop':
        break
    if int(user_input) > max_number:
        max_number = int(user_input)
print(max_number)