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

placevalue = {                                                                      #defines place value within my range (|1,000,000|)
    'Negative?': '0',
    'Millions':'0',
    'Hundred-Thousands':'0',
    'Ten-Thousands':'0',
    'Thousands':'0',
    'Hundreds':'0',
    'Tens':'0',
    'Ones':'0'
}


def paste_value(i, dictionary_name, placevalue):                                       #function to paste prefixes and suffixes
    for key, val in dictionary_name.items():
        if i == val:
            dictval = key

    if placevalue == 'none':
        print(dictval, end=" ")
    else:
        print(dictval + placevalue, end="")


def xteen(i, placevalue):                                                               #determines prefix if number is between 11-19
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

    paste_value(i, xteenvalue, placevalue)
    

def singledigitfunction(i, placevalue):                                                    #determines prefix if number is between 1-9
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

    paste_value(i, singledigitdict, placevalue)  


def doubledigitfunction(i, placevalue):                                                 #determines prefix if number is between 10-90
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

    paste_value(i, doubledigitdict, placevalue)



def isNegative():                                                                              #Determines if number is negative
    if placevalue['Negative?'] == '-':
        print('Negative ', end="")
    elif placevalue['Negative?'] == '0':
        pass


while True:                                                                                    #user interaction and exception handling 
    while True:
        user_input_number = input('\nEnter a number between -1000000 and 1000000: ')
        if user_input_number == 'quit':
            sys.exit('\nYou have successfully exited the program\n')
        try:
            user_input_number == int(user_input_number)
            break
        except:
            print('\nPlease enter a valid integer between -1000000 and 1000000')
            continue
    
    user_input_number = str(user_input_number)
    user_input_number = user_input_number.zfill(8)
    numtup = user_input_number

    #print(numtup) #Uncomment to see numtup

    if len(user_input_number) > 8:                                              #checks if input is in range
        print('\nNumber is out of range. Please enter a valid integer')
        continue

    indexcount = 0                                                                #determines placevalue
    for key in placevalue.keys():
            placevalue[key] = numtup[indexcount]
            indexcount += 1
    
    isNegative()                                                                  

    for i in placevalue: #millions                                                                #Begins process of naming the number
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



        








