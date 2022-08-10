

def find_pi():
    loop = False   
    pi = str(22/7)
    try:
        user_input_Nth = int(input('How many digits of pi do you want to see? '))
    except:
        print('Please enter a valid integer greater than 0')
        find_pi()
    index = user_input_Nth + 1
    while user_input_Nth > 0:
        print(pi[0:index])
        break
    loop = True
    while loop == True:
        option = input('\nWould you like to run the program again or quit?\n(1) Run program again\n(2) Quit\n'  ) 

        if option == '1':
            find_pi()
        elif option == '2':
            print('You have quit!')
            loop == False
            break
        else:
            print('\nPlease pick from the valid responses')
            continue
        

        


        
    
find_pi()