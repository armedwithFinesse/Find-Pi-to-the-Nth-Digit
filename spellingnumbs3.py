




placevalue = {
    'Millions':'0',
    'Hundred-Thousands':'0',
    'Ten-Thousands':'0',
    'Thousands':'0',
    'Hundreds':'0',
    'Tens':'0',
    'Ones':'0'
}

def singledigitfunction(i, placevalue):
    val = '0'
    if i == '0':
        val = " "
    elif i == '1':
        val = 'One' 
    elif i == '2':
        val = 'Two'
    elif i == '3':
        val = 'Three'
    elif i == '4':
        val = 'Four'
    elif i == '5':
        val = 'Five'
    elif i == '6':
        val = 'Six'
    elif i == '7':
        val = 'Seven'
    elif i == '8':
        val = 'Eight'
    elif i == '9':
        val = 'Nine'
   
    if i == '0':
        print(val)
    else:
        print(val + placevalue, end= "")   

def doubledigitfunction(i, placevalue):
    val = '0'
    if i == '0':
        val = " "
    elif i == '1':
        val = 'Ten' 
    elif i == '2':
        val = 'Twenty'
    elif i == '3':
        val = 'Thirty'
    elif i == '4':
        val = 'Fourty'
    elif i == '5':
        val = 'Fifty'
    elif i == '6':
        val = 'Sixty'
    elif i == '7':
        val = 'Seventy'
    elif i == '8':
        val = 'Eighty'
    elif i == '9':
        val = 'Ninety'
   
    if i == '0':
        print(val)
    else:
        print(val + placevalue, end= "")  


while True:
    try:
        user_input_number = int(input('Enter a number between 0 and 1000000: '))
        break
    except:
        print('Please enter a valid integer between 0 and 1000000')
        continue

user_input_number = str(user_input_number)
user_input_number = user_input_number.zfill(7)
numlist = (user_input_number[0], user_input_number[1], user_input_number[2],
user_input_number[3],user_input_number[4],user_input_number[5],user_input_number[6])

print(numlist)

if len(numlist) == 7:
    placevalue['Millions'] = numlist[0]
    placevalue['Hundred-Thousands'] = numlist[1]
    placevalue['Ten-Thousands'] = numlist[2]
    placevalue['Thousands'] = numlist[3]
    placevalue['Hundreds'] = numlist[4]
    placevalue['Tens'] = numlist[5]
    placevalue['Ones'] = numlist[6]
else:
    print('Something went horribly wrong')

print(placevalue)


'''
if len(numlist) == 7:
    placevalue['Millions'] = numlist[0]
    placevalue['Hundred-Thousands'] = numlist[1]
    placevalue['Ten-Thousands'] = numlist[2]
    placevalue['Thousands'] = numlist[3]
    placevalue['Hundreds'] = numlist[4]
    placevalue['Tens'] = numlist[5]
    placevalue['Ones'] = numlist[6]
elif len(numlist) == 6:
    placevalue['Millions'] = listplaceholder
    placevalue['Hundred-Thousands'] = numlist[0]
    placevalue['Ten-Thousands'] = numlist[1]
    placevalue['Thousands'] = numlist[2]
    placevalue['Hundreds'] = numlist[3]
    placevalue['Tens'] = numlist[4]
    placevalue['Ones'] = numlist[5]
    
elif len(numlist) == 5:
    placevalue['Millions'] = listplaceholder
    placevalue['Hundred-Thousands'] = listplaceholder
    placevalue['Ten-Thousands'] = numlist[0]
    placevalue['Thousands'] = numlist[1]
    placevalue['Hundreds'] = numlist[2]
    placevalue['Tens'] = numlist[3]
    placevalue['Ones'] = numlist[4]
elif len(numlist) == 4:
    placevalue['Millions'] = listplaceholder
    placevalue['Hundred-Thousands'] = listplaceholder
    placevalue['Ten-Thousands'] = listplaceholder
    placevalue['Thousands'] = numlist[0]
    placevalue['Hundreds'] = numlist[1]
    placevalue['Tens'] = numlist[2]
    placevalue['Ones'] = numlist[3]
elif len(numlist) == 3:
    placevalue['Millions'] = listplaceholder
    placevalue['Hundred-Thousands'] = listplaceholder
    placevalue['Ten-Thousands'] = listplaceholder
    placevalue['Thousands'] = listplaceholder
    placevalue['Hundreds'] = numlist[0]
    placevalue['Tens'] = numlist[1]
    placevalue['Ones'] = numlist[2]
elif len(numlist) == 2:
    placevalue['Millions'] = listplaceholder
    placevalue['Hundred-Thousands'] = listplaceholder
    placevalue['Ten-Thousands'] = listplaceholder
    placevalue['Thousands'] = listplaceholder
    placevalue['Hundreds'] = listplaceholder
    placevalue['Tens'] = numlist[0]
    placevalue['Ones'] = numlist[1]
elif len(numlist) == 1:
    placevalue['Millions'] = listplaceholder
    placevalue['Hundred-Thousands'] = listplaceholder
    placevalue['Ten-Thousands'] = listplaceholder
    placevalue['Thousands'] = listplaceholder
    placevalue['Hundreds'] = listplaceholder
    placevalue['Tens'] = listplaceholder
    placevalue['Ones'] = numlist[0]
'''

