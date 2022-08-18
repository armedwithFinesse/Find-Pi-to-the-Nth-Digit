import sys

while True:
    while True:
        userin = input('Enter any number greater than one: ')
        if userin == "quit":
            sys.exit('You have quit')
        try:
            userin = int(userin)
            break
        except:
            print('Enter a valid integer')
            continue
    
    if userin < 1:
        print('Number is out of range')
        continue


    val = userin
    stepcount = 0
    CollatzList = list()
    while val != 1:
        if val % 2 == 0:
            #number is even
            val = val//2
            stepcount += 1
            CollatzList.append(val)
            continue
        elif val % 2 != 0:
            #number is odd
            val = (val*3) + 1
            stepcount += 1
            CollatzList.append(val)
            continue

    print(f'It took {stepcount} steps to turn {userin} into 1')
    print(CollatzList)
            


