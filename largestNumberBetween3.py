# largest Number Between three number

a = int(input('Input Number1 : '))
b = int(input('Input Number2 : '))
c = int(input('Input Number3 : '))

# Method 1
# if a > b:
#     print('Largest Number = ', a)
# else:
#     if (b > c):
#         print('Largest Number = ', b)
#     else:
#         print('Largest Number =', c)

# Method 2
if (a > b) and (a > c):
    print('Largest Number = ', a)
elif b > c:
    print('Largest Number = ', b)
else:
    print('Largest Number =', c)
