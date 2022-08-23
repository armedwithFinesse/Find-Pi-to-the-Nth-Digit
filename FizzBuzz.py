
def isMultiple(i):
    if i % 3 == 0 and 1 % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)


for i in range(1,101): #prints 1-100
    isMultiple(i)



'''number = 0                                                   #This is another way to do the same thing.
while number < 101:
    if number % 3 == 0 and number % 5 == 0:
        print('multiple of both')
        number += 1
    elif number % 3 == 0:
        print('multiple of three')
        number += 1
    elif number % 5 == 0:
        print('multiple of five')
        number += 1
    else:
        print(number)
        number += 1'''


