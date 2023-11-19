from math import pi
print('Enter square/rectangle/circle/triangle')
figure = input()
if figure == 'square':
    print('Enter square line')
    face = float(input())
    area = face * face
    print(f"{area:.3f}")
elif figure == 'rectangle':
    print('Enter a')
    a = float(input())
    print('Enter b')
    b = float(input())
    area = a * b
    print(f"{area:.3f}")

elif figure == 'circle':
    r = float(input())
    area =  pi * r * r
    print(f"{area:.3f}")
elif figure == 'triangle':
    face = float(input())
    face_two = float(input())
    area =  (face * face_two ) / 2
    print(f"{area:.3f}")
