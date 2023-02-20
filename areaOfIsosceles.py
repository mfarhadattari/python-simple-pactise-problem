# Area of isosceles
# s = (a+b+c) / 2
# area = (s(s-a)(s-b)(s-c)) ** 0.5

a = float(input('a = ')) 
b = float(input('b = ')) 
c = float(input('c = ')) 

if (a+b > c) and (a+c> b) and (b+c> a) :
    s = (a + b + c) / 2 
    area = (s*(s-a)*(s-b)*(s-c) ) ** 0.5
    print('Area of isosceles: ', area)
else:
    print('Triangle is not possible. ')