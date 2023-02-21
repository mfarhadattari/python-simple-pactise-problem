numList = [10, 15, 69, 45, 46, 65, 6]

i = 0
lowest = numList[1]
largest = numList[1]

for i in numList :
    if (i > largest ):
        largest = i 
    else:
        largest = largest
        if(i < lowest):
            lowest = i
        else:
            lowest = lowest
        

print('largest', largest)
print('lowest', lowest)