import math

print('''

__      __      _                      
\ \    / / ___ | | __  ___  _ __   ___ 
 \ \/\/ / / -_)| |/ _|/ _ \| '  \ / -_)
  \_/\_/  \___||_|\__|\___/|_|_|_|\___|
----------------------------------------
         Prime Factor Finder!


''')


user = int((input('Enter a number: ')))
factors = list()
x = True
while x == True:
    if user % 2 == 0:
        factors.append(2)
        user = user / 2
        
    elif user % 3 == 0:
        factors.append(3)
        user = user/3

    elif user % 5 == 0:
        factors.append(5)
        user = user/5
        rngsqrt = math.sqrt(user) + 1
        for i in range(7,int(rngsqrt)):
            if user % i == 0:
                factors.append(i)
                user/i

    else:
        print(factors)
        x == False
        break

