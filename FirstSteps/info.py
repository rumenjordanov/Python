

my_name= "Rumen Jordanov"  #string - tekst
items_qty = 3   #int - cqlo chislo
total_price = 95.13   #float - realno chislo s zapetaq


first_name = input("Enter your weight:") #input vinagi e string
print("Tejish " + first_name + " kila")



user_input = int(input())
print(type(user_input))

a = int(input())  #int se smenq s float ( za realni chisla
area = a * a
print(area)

# f se slaga na print za po lesno
name = input()
project = int(input())
hours = project * 3
print(f"The architect {name} will need {hours} hours to complete {project} project/s.")

#ima dva tipa deleniq / i //  ( / - 6.30 , //- 6 )
# % - kolko puti se pobira . a = 7 b = 2 product = a % b = 7 % 2 = 3.


cena = 5
druga = 3
cena +=\ druga

-=
*=
/=


10 == 10
(True)

3>2
(True)


10 != 10  # razlichno li e
(False)


my_age = 16
is_age_legal = my_age >= 18
print(is_age_legal)

my_age = 18
if my_age >= 18:
    print("Have Fun!")
    print("See content")


grade = float(input())
if grade >= 5.5:
    print("Excellent!")
elif grade < 4:
    print("Losho")
else:
    print("Mid")


from math import floor, ceil  '''floor nagore , ceil nadolu'''
number = 4.24421
print(ceil(number))

number = 4.5424245                  '''zakruglqne sled zapetaikata , promenqme chisloto sled number'''
print(round(number,3))


print(f"{area:.3f}")            # kolko sled zapetaikata da dade chislo



"""Izpolzvane na IF,ELIF,ELSE"""
if day == 1:
    result = "Monday"
elif day == 2:
    result = "Tuesday"
elif day == 3:
    result = "Wednesday"
else:
    result = "Error"
print(f"{result}")


""" Izpolzvane na OR"""
if day == "Monday" or day == "Tuesday" or day == "Wednesday":
    print("Working day")
elif day == "Nedelq" or day == "Subota":
    print("pochivka")
else:
    print("ne e den")


"""IF V IF"""
if sex == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")


"""NOT IN"""
cities = "Sofia, Varna, Plovdiv"
if city_name not in cities:
    print("error")



"""FOR I IN RANGE"""
for i in range(1, 101):
    print(i)

"""PASS"""
for i in range(1, 101):
    if i == 5:
        pass
    else:
        print(i)

"""S PROMENLIVA"""
n = int(input())
for i in range(1, n + 1):
    print(i)

 '''NA EDIN RED'''
n = int(input())
for i in range(1, n + 1):
print(promenliva, end = "")


'''PREZ KOLKO DA SA CHISLATA - TRETOTO CHISLO V RANGE'''
n = int(input())
for i in range(1, n + 1, 3):
    print(i)

n = int(input())
for i in range(n, 0, -1):
    print(i)

"""dumi"""
word = str(input())
for i in range(0, len(word)):
    print(word[i]) # podavame poziciq s []



user_input = input()
total = 0
for i in range(0, len(user_input)):
    char = user_input[i]
if char == "a":
    total += 1



user_input = input()
for i in range(0, len(user_input)):
    print(user_input[i])


n = int(input())
for i in range(n):
    user_input = int(input())