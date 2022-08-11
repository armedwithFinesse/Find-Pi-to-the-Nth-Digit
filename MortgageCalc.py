import math

print('''

__      __      _                      
\ \    / / ___ | | __  ___  _ __   ___ 
 \ \/\/ / / -_)| |/ _|/ _ \| '  \ / -_)
  \_/\_/  \___||_|\__|\___/|_|_|_|\___|
----------------------------------------
        Floor Plan Calculator!


''')



userlen = float(input('Please enter the length of the floor you wish to cover (sq.ft): '))
userwidth = float(input('Please enter the width of the floor you wish to cover (sq.ft): '))
userprice = float(input('Please enter the price of flooring per square foot: '))

area = userlen * userwidth
price = userprice * area
messege = ('The total cost of the flooring is ${}' )

print(messege.format(price))