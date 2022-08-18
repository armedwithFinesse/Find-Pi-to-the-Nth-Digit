import sys
'''
need to add support for floats (?)
'''

print('''
▀█▄   ▀█▀                     ▀██                          ▄█▀▀▀▄█                   ▀██  ▀██                  
 █▀█   █  ▄▄▄ ▄▄▄  ▄▄ ▄▄ ▄▄    ██ ▄▄▄    ▄▄▄▄  ▄▄▄ ▄▄      ██▄▄  ▀  ▄▄▄ ▄▄▄    ▄▄▄▄   ██   ██    ▄▄▄▄  ▄▄▄ ▄▄  
 █ ▀█▄ █   ██  ██   ██ ██ ██   ██▀  ██ ▄█▄▄▄██  ██▀ ▀▀      ▀▀███▄   ██▀  ██ ▄█▄▄▄██  ██   ██  ▄█▄▄▄██  ██▀ ▀▀ 
 █   ███   ██  ██   ██ ██ ██   ██    █ ██       ██        ▄     ▀██  ██    █ ██       ██   ██  ██       ██     
▄█▄   ▀█   ▀█▄▄▀█▄ ▄██ ██ ██▄  ▀█▄▄▄▀   ▀█▄▄▄▀ ▄██▄       █▀▄▄▄▄█▀   ██▄▄▄▀   ▀█▄▄▄▀ ▄██▄ ▄██▄  ▀█▄▄▄▀ ▄██▄  
                                                                     ██                                        
                                                                    ▀▀▀▀                                                                                
                                            Enter "quit" to exit

''')




placevalue = {
    'Negative?': '0',
    'Millions':'0',
    'Hundred-Thousands':'0',
    'Ten-Thousands':'0',
    'Thousands':'0',
    'Hundreds':'0',
    'Tens':'0',
    'Ones':'0'
}


def xteen(i, placevalue):

    xteenvalue = {
        "Eleven":"1",
        'Twelve': '2',
        'Thirteen':'3',
        'Fourteen': '4',
        'Fifteen': '5',
        'Sixteen': '6',
        'Seventeen':'7',
        'Eighteen': '8',
        'Nineteen': '9'
    }
    for key, val in xteenvalue.items():
        if i == val:
            xteendictvalue = key

    if placevalue == 'none':
        print(xteendictvalue, end="")
    else:
        print(xteendictvalue + placevalue, end="")
    

def singledigitfunction(i, placevalue):
    singledigitdict = {
        'One':'1',
        'Two': '2',
        'Three':'3',
        'Four':'4',
        'Five':'5',
        'Six':'6',
        'Seven': '7',
        'Eight': '8',
        'Nine': '9',

    }
    for key, val in singledigitdict.items():
        if i == val:
            dictval = key
   
    if placevalue == 'none':
        print(dictval, end="")
    else:
        print(dictval + placevalue, end="")   


def doubledigitfunction(i, placevalue):
    doubledigitdict = {
        "Ten":"1",
        'Twenty': '2',
        'Thirty':'3',
        'Fourty': '4',
        'Fifty': '5',
        'Sixty': '6',
        'Seventy':'7',
        'Eighty': '8',
        'Ninety': '9'
    }

    for key, val in doubledigitdict.items():
        if i == val:
            dictvaldouble = key

    if placevalue == 'none':
        print(dictvaldouble, end=" ")
    else:
        print(dictvaldouble + placevalue, end="")  


def isNegative():
    if placevalue['Negative?'] == '-':
        if len(user_input_number) > 8:
            global out_of_range
            out_of_range = True
            print('\nNumber is out of range. Please enter a valid integer')
        else:
            print('Negative ', end="")
    elif placevalue['Negative?'] == '0':
        pass
    else:
        out_of_range = True
        print('\nNumber is out of range. Please enter a valid integer')
        

global user_input_number
user_input_number = ""
while True:
    if user_input_number == 'quit': 
        sys.exit()
    out_of_range = False
    while True:
        user_input_number = input('\nEnter a number between -1000000 and 1000000: ')
        if user_input_number == 'quit':
            sys.exit()
        try:
            user_input_number == int(user_input_number)
            break
        except:
            print('\nPlease enter a valid integer between -1000000 and 1000000')
            continue
            
    
    
    user_input_number = str(user_input_number)
    user_input_number = user_input_number.zfill(8)
    numlist = (user_input_number[0], user_input_number[1], user_input_number[2],
    user_input_number[3],user_input_number[4],user_input_number[5],user_input_number[6], user_input_number[7])


    #print(numlist) #Uncomment to show integer split up into placevalues
    #print(user_input_number) #Uncomment to show user input value

    if len(numlist) == 8:
        placevalue['Negative?'] = numlist[0]
        placevalue['Millions'] = numlist[1]
        placevalue['Hundred-Thousands'] = numlist[2]
        placevalue['Ten-Thousands'] = numlist[3]
        placevalue['Thousands'] = numlist[4]
        placevalue['Hundreds'] = numlist[5]
        placevalue['Tens'] = numlist[6]
        placevalue['Ones'] = numlist[7]
    else:
        print('Something went horribly wrong')

    isNegative()
    try:
        if out_of_range == True:
            continue
    except:
        pass


    for i in placevalue: #millions
        if placevalue['Millions'] != '0': #Millions place
            singledigitfunction(placevalue['Millions'], ' Million ')
            break



    for i in placevalue: #hundred thousands

        if placevalue['Hundred-Thousands'] != '0' and placevalue['Ten-Thousands'] == '0' and placevalue['Thousands'] != '0': 
            singledigitfunction(placevalue['Hundred-Thousands'], ' Hundred-and ')
        elif placevalue['Hundred-Thousands'] != '0' and placevalue['Ten-Thousands'] == '0' and placevalue['Thousands'] == '0':
            singledigitfunction(placevalue['Hundred-Thousands'], ' Hundred-Thousand ')
        elif placevalue['Hundred-Thousands'] != '0' and placevalue['Ten-Thousands'] != '0':
            singledigitfunction(placevalue['Hundred-Thousands'], ' Hundred ')
        elif placevalue['Hundred-Thousands'] == '0':
            break
        else:
            singledigitfunction(placevalue['Hundred-Thousands'], ' Hundred-Thousand ')
        break


    for i in placevalue: #ten thousands

        if placevalue['Ten-Thousands'] == '1' and placevalue['Thousands'] > '0': 
            xteen(placevalue['Thousands'], ' Thousand ') #sep function needed to definte 11 - 19 thousand
        elif placevalue['Ten-Thousands'] == '1' and placevalue['Thousands'] == '0': 
            doubledigitfunction(placevalue['Ten-Thousands'], ' Thousand ') # ten thousand
        elif placevalue['Ten-Thousands'] > '1' and placevalue['Thousands'] == '0':
            doubledigitfunction(placevalue['Ten-Thousands'], ' Thousand ') 
        elif placevalue['Ten-Thousands'] > '1' and placevalue['Thousands'] >= '0':
            doubledigitfunction(placevalue['Ten-Thousands'], 'none') #ex: "fifty" thousand
        elif placevalue['Ten-Thousands'] == '0':
            break 
        break




    for i in placevalue: #thousands

        if placevalue['Thousands'] != '0' and placevalue['Hundreds'] >= '0': 
            if placevalue['Ten-Thousands'] == '1':
                break
            else:
                singledigitfunction(placevalue['Thousands'], ' Thousand ')

        break


    for i in placevalue: #hundreds

        if placevalue['Hundreds'] != '0':
            singledigitfunction(placevalue['Hundreds'], ' Hundred ')
        break

    for i in placevalue: #tens

        if placevalue['Tens'] == "1" and placevalue['Ones'] > '0':
            xteen(placevalue['Ones'], 'none') #sep function needed to definte 11 - 19 
        elif placevalue['Tens'] != '0':
            doubledigitfunction(placevalue['Tens'], 'none')
        elif placevalue['Tens'] == '0' and placevalue['Hundreds'] > '0' and placevalue['Ones'] != '0':
            doubledigitfunction(placevalue['Tens'], ' and ')
        break

    for i in placevalue: #ones

        if placevalue['Tens'] == '1':
            break
        elif placevalue['Ones'] != '0':
            singledigitfunction(placevalue['Ones'], 'none')
            break
        elif placevalue['Ones'] == '0' and placevalue['Tens'] == '0' and placevalue['Hundreds']  == '0' and placevalue['Thousands']  == '0' and placevalue['Ten-Thousands']  == '0' and placevalue['Hundred-Thousands']  == '0' and placevalue['Millions']  == '0' :
            print('Zero')
            break



        








