# quadratic equation
# ax**2 + bx + c =0
# d= b**2 -4ac
# x = (-b(+-)((d)**0.5)) / 2a

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

d = pow(b, 2) - (4 * a * c)

if (d > 0):
    x1 = -b + ((d)**0.5)
    x1 = -b - ((d)**0.5)
    print('x1 = ', x1)
    print('x2 = ', x2)

elif (d == 0):
    x = -b / (2 * a)
    print('x= ', x)
else:
    print('Imaginary Roots')
