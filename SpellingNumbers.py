


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

def xteen(i, placevalue):
    xteenvalue = 0
    while True:
        if i == '1':
            xteenvalue = 'Eleven'
            break
        elif i == '2':
            xteenvalue = 'Twelve'
            break
        elif i == '3':
            xteenvalue = 'Thirteen'
            break
        elif i == '4':
            xteenvalue = 'Fourteen'
            break
        elif i == '5':
            xteenvalue = 'Fifteen'
            break
        elif i == '6':
            xteenvalue = 'Sixteen'
            break
        elif i == '7':
            xteenvalue = 'Seventeen'
            break
        elif i == '8':
            xteenvalue = 'Eighteen'
            break
        elif i == '9':
            xteenvalue = 'Nineteen'
            break
        else:
            break


    if placevalue == 'noval':
        print(xteenvalue, end=" ")
    else:
        print(xteenvalue + placevalue, end=" ")
    




def singledigitplacevalue_no_cond(placevalue):
    while True:
        if i == '0':
            value = " "
            break
        elif i == '1':
            value = 'One' 
            break
        elif i == '2':
            value = 'Two'
            break
        elif i == '3':
            value = 'Three'
            break
        elif i == '4':
            value = 'Four'
            break
        elif i == '5':
            value = 'Five'
            break
        elif i == '6':
            value = 'Six'
            break
        elif i == '7':
            value = 'Seven'
            break
        elif i == '8':
            value = 'Eight'
            break
        elif i == '9':
            value = 'Nine'
            break
        else:
            break
    if placevalue == 'noval':
        print(value, end=" ") 
    else:
        print(value + placevalue, end=" ")  
        
        


def singledigitplacevalue(placevalue):

      for i in user_input_number:

        if i == '0':
            value = " "
        elif i == '1':
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
        if placevalue == 'noval':
            print(value, end=" ")
            break
        else:
            print(value + placevalue, end=" ")  
            break 
def doubledigitplacevalue(placevalue):
    for i in user_input_number:
        if i == '0':
            value = " "
        elif i == '1':
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
        if placevalue == 'noval':
            print(value, end=" ")
            break
        else:
            print(value + placevalue, end=" ")  
            break 

def doubledigitplacevalue_no_cond(placevalue):
    while True:
        if i == '0':
            value = " "
            break
        elif i == '1':

            value = 'Ten' 
            break
        elif i == '2':
            value = 'Twenty'
            break
        elif i == '3':
            value = 'Thirty'
            break
        elif i == '4':
            value = 'Fourty'
            break
        elif i == '5':
            value = 'Fifty'
            break
        elif i == '6':
            value = 'Sixty'
            break
        elif i == '7':
            value = 'Seventy'
            break
        elif i == '8':
            value = 'Eighty'
            break
        elif i == '9':
            value = 'Ninety'
            break
        else:
            break
    if placevalue == 'noval':
        print(value, end=" ")
        
    else:
        print(value + placevalue, end=" ")  

        





begtup = ('m','ht','tt','t','h','t','o')

while True:
    try:
        user_input_number = int(input('Enter a number between 0 and 1000000: '))
        break
    except:
        print('Please enter a valid integer between 0 and 1000000')
        continue
    
user_input_number = str(user_input_number)
user_input_number = tuple(user_input_number)
if len(user_input_number) == 7: #millions
    singledigitplacevalue(' Million')


#========================================================================================================================IN PROGRESS
elif len(user_input_number) == 6: # hundred -thousands

    for i in user_input_number:
        if user_input_number[1] == '0' and user_input_number [2] == '0':
            singledigitplacevalue(' Hundred-Thousand')
            newvar = 1
            break
        elif user_input_number[1] != '0' and user_input_number[2] != '0':
            singledigitplacevalue(' Hundred and')
            break
        elif user_input_number[1] != '0' and user_input_number[2] <= '0':
            singledigitplacevalue(' Hundred and')
            break
        else:
            singledigitplacevalue(' Hundred')
            break
    for i in user_input_number:
        if user_input_number[2] == '0' and newvar != 1:
            doubledigitplacevalue('-Thousand') 
            rvar = 1
            break
        elif user_input_number[1] == '1' and user_input_number[2] == '0':
            singledigitplacevalue('-Thousand') #thousand
            break
        elif user_input_number[1] == '1' and user_input_number[2] > '0' and user_input_number[2] <= '9':
            xteen(user_input_number[2], '- Thousand')
            rvar = 3
            break
        elif newvar != 1:
            doubledigitplacevalue('noval')
            rvar = 1
            break
       
    count = 0
    for i in user_input_number:
        if i == user_input_number[2] and user_input_number[2] != '0' and rvar == 1:
            #1-9 thou
            singledigitplacevalue_no_cond(' Thousand')
            break
        elif i == user_input_number[2] and user_input_number[2] == '0' and rvar == 0:
            singledigitplacevalue_no_cond('noval')
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[3] and user_input_number[3] != '0':
            singledigitplacevalue_no_cond(' Hundred')
            break
        elif i == user_input_number[3] and user_input_number[3] == '0':
            singledigitplacevalue_no_cond('noval')
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[4] and user_input_number[4] == '1' and user_input_number[5] != '0':
            #some loop to find numbers eleven through nineteen
            xteen(user_input_number[5], 'noval')
            count += 1
            movcount = 1
            break
        elif i == user_input_number[4] and user_input_number[4] >= '0' and user_input_number[5] >= '0' and count == 0:
            doubledigitplacevalue_no_cond('noval')
            movcount = 2
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[5] and movcount == 2:
            singledigitplacevalue_no_cond('noval')
            break
        elif i == user_input_number[5] and movcount == 1:
            break
        else:
            continue






    '''for i in user_input_number:
        if i == user_input_number[2] and user_input_number[2] != '0' and rvar == 1:
            doubledigitplacevalue_no_cond(' Thousand')
            break
        elif i == user_input_number[2] and user_input_number == '0' and rvar == 2:
            doubledigitplacevalue_no_cond('noval')
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[3] and user_input_number[3] != '0':
            singledigitplacevalue_no_cond(' Hundred')
            break
        elif i == user_input_number[3] and user_input_number[3] == '0':
            singledigitplacevalue_no_cond('noval')
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[4] and user_input_number[4] != '0':
            pass
        else:
            continue'''



#===========================================================================================================================works===========================
elif len(user_input_number) == 5: #ten-thousands
    for i in user_input_number:
        if user_input_number[1] == '0':
            doubledigitplacevalue('-Thousand') #11-90 thou
            rvar = 1
            break
        elif user_input_number[0] == '1' and user_input_number[1] == '0':
            singledigitplacevalue('noval') #thousand
            break
        elif user_input_number[0] == '1' and user_input_number[1] > '0' and user_input_number[1] <= '9':
            xteen(user_input_number[1], '-Thousand')
            rvar = 3
            break
        else:
            doubledigitplacevalue('noval')
            rvar = 1
            break
       
    count = 0
    for i in user_input_number:
        if i == user_input_number[1] and user_input_number[1] != '0' and rvar == 1:
            #1-9 thou
            singledigitplacevalue_no_cond(' Thousand')
            break
        elif i == user_input_number[1] and user_input_number[1] == '0' and rvar == 0:
            singledigitplacevalue_no_cond('noval')
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[2] and user_input_number[2] != '0':
            singledigitplacevalue_no_cond(' Hundred')
            break
        elif i == user_input_number[2] and user_input_number[2] == '0':
            singledigitplacevalue_no_cond('noval')
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[3] and user_input_number[3] == '1' and user_input_number[4] != '0':
            #some loop to find numbers eleven through nineteen
            xteen(user_input_number[4], 'noval')
            count += 1
            movcount = 1
            break
        elif i == user_input_number[3] and user_input_number[3] >= '0' and user_input_number[4] >= '0' and count == 0:
            doubledigitplacevalue_no_cond('noval')
            movcount = 2
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[4] and movcount == 2:
            singledigitplacevalue_no_cond('noval')
            break
        elif i == user_input_number[4] and movcount == 1:
            break
        else:
            continue




    '''for i in user_input_number:
        if i == user_input_number[2] and user_input_number[2] != '0':
            singledigitplacevalue_no_cond(' Hundred')
            break
        elif i == user_input_number[2] and user_input_number[2] == '0':
            singledigitplacevalue_no_cond('noval')
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[3] and user_input_number[3] != '0':
            doubledigitplacevalue_no_cond('noval')
            break
        elif i == user_input_number[3] and user_input_number[3] == '0':
            doubledigitplacevalue_no_cond('Ten/Pending')
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[4]:
            singledigitplacevalue_no_cond('noval')
            break
        else:
            continue'''


    














    '''thousands_count = 1
    hundreds_count = 1
    tens_count = 1
    ones_count = 1
    for i in user_input_number:
        if i == user_input_number[1] and thousands_count == 1:
            if user_input_number[1] != '0':
                singledigitplacevalue_no_cond(' Thousand') 
            else:
                singledigitplacevalue_no_cond('noval')
            thousands_count +=1 
        if i == user_input_number[2] and hundreds_count == 1:
            if user_input_number[2] != '0':
                singledigitplacevalue_no_cond(' Hundred')
            else:
                singledigitplacevalue_no_cond('noval')
            hundreds_count += 1
        if i == user_input_number[3] and tens_count == 1:
            doubledigitplacevalue_no_cond('noval')
            tens_count += 1
        if i == user_input_number[4] and ones_count == 1:
            singledigitplacevalue_no_cond('noval')
            ones_count += 1
            break'''
        


#===============================================================================================================works=======================================

elif len(user_input_number) == 4: #thousands
    singledigitplacevalue(' Thousand') 
    count = 0
    for i in user_input_number:
        if i == user_input_number[1] and user_input_number[1] != '0':
            singledigitplacevalue_no_cond(' Hundred')
            break
        elif i == user_input_number[1] and user_input_number[1] == '0':
            singledigitplacevalue_no_cond('noval')
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[2] and user_input_number[2] == '1' and user_input_number[3] != '0':
            #some loop to find numbers eleven through nineteen
            xteen(user_input_number[3], 'noval')
            count += 1
            movcount = 1
            break
        elif i == user_input_number[2] and user_input_number[2] >= '0' and user_input_number[3] >= '0' and count == 0:
            doubledigitplacevalue_no_cond('noval')
            movcount = 2
            break
        else:
            continue
    for i in user_input_number:
        if i == user_input_number[3] and movcount == 2:
            singledigitplacevalue_no_cond('noval')
            break
        elif i == user_input_number[3] and movcount == 1:
            break
        else:
            continue



    '''hundreds_count = 1
    tens_count = 1
    ones_count = 1
    for i in user_input_number:
        if i == user_input_number[1] and hundreds_count == 1:
            if user_input_number[1] != 0:
                singledigitplacevalue_no_cond(' Hundred')
            else:
                singledigitplacevalue_no_cond('noval')
            hundreds_count += 1
        if i == user_input_number[2] and tens_count == 1:
            if user_input_number[2] != 0:
                doubledigitplacevalue_no_cond(' Hundred')
            else:
                doubledigitplacevalue_no_cond('noval')
            tens_count += 1
        if i == user_input_number[3] and ones_count == 1:
            singledigitplacevalue_no_cond('noval')
            ones_count += 1
            break
        else:
            continue'''





#==================================================================================================================works====================================

elif len(user_input_number) == 3: #hundreds
    singledigitplacevalue(' Hundred') 
    count = 0
    for i in user_input_number:
        
        if i == user_input_number[1] and user_input_number[1] == '1' and user_input_number[2] != '0':
            #some loop to find numbers eleven through nineteen
            xteen(user_input_number[2], 'noval')
            count += 1
            break
        elif i == user_input_number[1] and user_input_number[1] >= '0' and user_input_number[2] >= '0' and count == 0:
            doubledigitplacevalue_no_cond('noval')
            break
        else:
            continue

    if count == 0:
        for i in user_input_number:
            if i == user_input_number[2]:
                singledigitplacevalue_no_cond('noval')
                break
            else:
                continue

    '''for i in user_input_number:
        if i == user_input_number[1]:
                doubledigitplacevalue_no_cond('noval')
        if i == user_input_number[2]:
            singledigitplacevalue_no_cond('noval')
            
        else:
            break'''

    




#========================================================================================================works
elif len(user_input_number) == 2: #tens
    doubledigitplacevalue('noval')
    for i in user_input_number:
        if i == user_input_number[1]:
            singledigitplacevalue_no_cond('noval')
            break
        else:
            continue
elif len(user_input_number) == 1: #ones 
    singledigitplacevalue('noval')
















