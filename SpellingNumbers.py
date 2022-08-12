from telnetlib import theNULL
from tkinter import Place


'''i want the user to input any number between 0 and 1 million ( as whole, positive integers).
then I want the program to return the english spelled version of that integer.
I assume first i must have a collection(set, list, tuple, dict) of numbers between 0 and 1,000,000.
Then I have to define the place value of any number up to and including 1,000,000 (millions place,Hundred Thousands place, ten thousands place,
 thousands place, hundreds place, tens place, ones Place)
 Then I have to write a conditional that if the users input contains something in the millions place, I need to concatenate a string that is like
 1 = one, one + million.
  If users input contains something in the hundred-thousands place, I concatenate both like so: 3 = three hundred thousand, three + hundred thousand

  then one +million + three +hundred-thousand....etc for all place values
  
  =====
  perhaps I can find place value by the length of the user input number
  
  '''



begtup = ('m','ht','tt','t','h','t','o')


user_input_number = input('Enter a number between 0 and 1000000: ')
user_input_number = tuple(user_input_number)
if len(user_input_number) == 7: #millions
    placevalue = ' Million'
    for i in user_input_number:
        if i == '1':
            value = 'One' 
        elif i == '2':
            value = 'Two'
        elif i == '3':
            value = 'Three'
        elif i == '4':
            value = 'Four'
        elif i == '5':
            value = 'Five'
        elif i == '6':
            value = 'Six'
        elif i == '7':
            value = 'Seven'
        elif i == '8':
            value = 'Eight'
        elif i == '9':
            value = 'Nine'
        print(value + placevalue)  
        break 
elif len(user_input_number) == 6: # hundred -thousands
    placevalue = ' Hundred-Thousand'
    for i in user_input_number:
        if i == '1':
            value = 'One' 
        elif i == '2':
            value = 'Two'
        elif i == '3':
            value = 'Three'
        elif i == '4':
            value = 'Four'
        elif i == '5':
            value = 'Five'
        elif i == '6':
            value = 'Six'
        elif i == '7':
            value = 'Seven'
        elif i == '8':
            value = 'Eight'
        elif i == '9':
            value = 'Nine'
        print(value + placevalue)  
        break 
elif len(user_input_number) == 5: #ten-thousands
    placevalue = '-Thousand'
    for i in user_input_number:
        if i == '1':
            value = 'Ten' 
        elif i == '2':
            value = 'Twenty'
        elif i == '3':
            value = 'Thirty'
        elif i == '4':
            value = 'Fourty'
        elif i == '5':
            value = 'Fifty'
        elif i == '6':
            value = 'Sixty'
        elif i == '7':
            value = 'Seventy'
        elif i == '8':
            value = 'Eighty'
        elif i == '9':
            value = 'Ninety'
        print(value + placevalue)  
        break 

    
elif len(user_input_number) == 4: #thousands
    placevalue = ' Thousand'
    for i in user_input_number:
        if i == '1':
            value = 'One' 
        elif i == '2':
            value = 'Two'
        elif i == '3':
            value = 'Three'
        elif i == '4':
            value = 'Four'
        elif i == '5':
            value = 'Five'
        elif i == '6':
            value = 'Six'
        elif i == '7':
            value = 'Seven'
        elif i == '8':
            value = 'Eight'
        elif i == '9':
            value = 'Nine'
        print(value + placevalue)  
        break 
elif len(user_input_number) == 3: #hundreds
    placevalue = ' Hundred'
    for i in user_input_number:
        if i == '1':
            value = 'One' 
        elif i == '2':
            value = 'Two'
        elif i == '3':
            value = 'Three'
        elif i == '4':
            value = 'Four'
        elif i == '5':
            value = 'Five'
        elif i == '6':
            value = 'Six'
        elif i == '7':
            value = 'Seven'
        elif i == '8':
            value = 'Eight'
        elif i == '9':
            value = 'Nine'
        print(value + placevalue)  
        break  
elif len(user_input_number) == 2: #tens
    for i in user_input_number:
        if i == '1':
            value = 'Ten' 
        elif i == '2':
            value = 'Twenty'
        elif i == '3':
            value = 'Thirty'
        elif i == '4':
            value = 'Fourty'
        elif i == '5':
            value = 'Fifty'
        elif i == '6':
            value = 'Sixty'
        elif i == '7':
            value = 'Seventy'
        elif i == '8':
            value = 'Eighty'
        elif i == '9':
            value = 'Ninety'
        print(value)  
        break 
elif len(user_input_number) == 1: #ones
    #placevalue = ' '
    for i in user_input_number:
        if i == '1':
            value = 'One' 
        elif i == '2':
            value = 'Two'
        elif i == '3':
            value = 'Three'
        elif i == '4':
            value = 'Four'
        elif i == '5':
            value = 'Five'
        elif i == '6':
            value = 'Six'
        elif i == '7':
            value = 'Seven'
        elif i == '8':
            value = 'Eight'
        elif i == '9':
            value = 'Nine'
        print(value)  
        break 

else:
    print('need to add one to len of user input')










'''placevaluedict = {
            
            "Millions":begtup[0],
            "Hundred-Thousand":begtup[1],
            "Ten-thousand":begtup[2],
            "Thousand": begtup[3],
            "Hundred":begtup[4],
            "Ten":begtup[5],
            "One":begtup[6]
            }

while True:
    try:
        print(placevaluedict)
        print(user_input_number)
        break
    except:
        print('Enter a valid integer')
        continue'''







