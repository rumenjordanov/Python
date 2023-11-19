food = int(input())
food = food * 1000
left_food = food

while True:
    input_user = input()
    if input_user == 'Adopted':
        if left_food >= 0:
            print(f'Food is enough! Leftovers: {left_food} grams.')
        else:
            print(f'Food is not enough. You need {abs(left_food)} grams more.')
        break
    else:
        eaten = int(input_user)
        left_food -= eaten