x = int(input('x : '))
y = int(input('y : '))
z = int(input('z : '))

if 0 in [x,y,z]:
    print('Not a triangle')
    exit(1)

if x == y == z:
    print ('Equilateral Triangle')
elif x==y or x==z or y==z:
    print ('Isoceles Triangle')
else:
    print ('Scalene Triangle')