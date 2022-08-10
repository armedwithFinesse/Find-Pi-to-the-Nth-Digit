import math

print('''
__      __      _                      
\ \    / / ___ | | __  ___  _ __   ___ 
 \ \/\/ / / -_)| |/ _|/ _ \| '  \ / -_)
  \_/\_/  \___||_|\__|\___/|_|_|_|\___|
----------------------------------------
Calculating the Fibonacci Sequence to the 
    nth degree using Binet's Forumla

''')

golden_ratio = (1 + 5 ** 0.5)/2
user = int(input('Enter a number (n): '))                                          
                                                                #binets_formula = ((golden_ratio**user) - ((1 - golden_ratio)**user))/math.sqrt(5)
userlist = list()
for i in range(user+1):
    binets_formula_i = ((golden_ratio**i) - ((1 - golden_ratio)**i))/math.sqrt(5)
    userlist.append(int(binets_formula_i))




print('\n',userlist,'\n')
print('Finished!\n')




