from ast import excepthandler
from tempfile import TemporaryFile


board = [['.', '.', '.', '.', '.', '.', '.', '.'],['P','P','P','P','P','P','P','P',],['R',  'N', 'B',  'K',  'Q',  'B',  'N',  'R']]

notation_letter = '    A  B  C  D  E  F  G  H'
notation_number = ['1', '2', '3', '4', '5', '6', '7','8']     


notation_dict_row_eight = {'A8':board[2][0],'B8':board[2][1],'C8':board[2][2],'D8':board[2][3],'E8':board[2][4],'F8':board[2][5],'G8':board[2][6],'H8':board[2][7]}
notation_dict_row_seven = {'A7':board[1][0],'B7':board[1][1],'C7':board[1][2],'D7':board[1][3], 'E7':board[1][4],'F7':board[1][5],'G7':board[1][6],'H7':board[1][7]}
notation_dict_row_six = {'A6':board[0][0],'B6':board[0][1],'C6':board[0][2],'D6':board[0][3], 'E6':board[0][4],'F6':board[0][5],'G6':board[0][6],'H6':board[0][7]}
notation_dict_row_five = {'A5':board[0][0],'B5':board[0][1],'C5':board[0][2],'D5':board[0][3], 'E5':board[0][4],'F5':board[0][5],'G5':board[0][6],'H5':board[0][7]}
notation_dict_row_four = {'A4':board[0][0],'B4':board[0][1],'C4':board[0][2],'D4':board[0][3], 'E4':board[0][4],'F4':board[0][5],'G4':board[0][6],'H4':board[0][7]}
notation_dict_row_three = {'A3':board[0][0],'B3':board[0][1],'C3':board[0][2],'D3':board[0][3], 'E3':board[0][4],'F3':board[0][5],'G3':board[0][6],'H3':board[0][7]}
notation_dict_row_two = {'A2':board[1][0],'B2':board[1][1],'C2':board[1][2],'D2':board[1][3], 'E2':board[1][4],'F2':board[1][5],'G2':board[1][6],'H2':board[1][7]}
notation_dict_row_one = {'A1':board[2][0],'B1':board[2][1],'C1':board[2][2],'D1':board[2][3],'E1':board[2][4],'F1':board[2][5],'G1':board[2][6],'H1':board[2][7]}


notation_list = [notation_dict_row_eight, notation_dict_row_seven, notation_dict_row_six, notation_dict_row_five, notation_dict_row_four, notation_dict_row_three, notation_dict_row_two, notation_dict_row_one]

'''notation_dict_full = {

notation_dict_row_eight : {'A8':board[2][0],'B8':board[2][1],'C8':board[2][2],'D8':board[2][3],'E8':board[2][4],'F8':board[2][5],'G8':board[2][6],'H8':board[2][7]},
notation_dict_row_seven : {'A7':board[1][0],'B7':board[1][1],'C7':board[1][2],'D7':board[1][3], 'E7':board[1][4],'F7':board[1][5],'G7':board[1][6],'H7':board[1][7]},
notation_dict_row_six : {'A6':board[0][0],'B6':board[0][1],'C6':board[0][2],'D6':board[0][3], 'E6':board[0][4],'F6':board[0][5],'G6':board[0][6],'H6':board[0][7]},
notation_dict_row_five : {'A5':board[0][0],'B5':board[0][1],'C5':board[0][2],'D5':board[0][3], 'E5':board[0][4],'F5':board[0][5],'G5':board[0][6],'H5':board[0][7]},
notation_dict_row_four : {'A4':board[0][0],'B4':board[0][1],'C4':board[0][2],'D4':board[0][3], 'E4':board[0][4],'F4':board[0][5],'G4':board[0][6],'H4':board[0][7]},
notation_dict_row_three : {'A3':board[0][0],'B3':board[0][1],'C3':board[0][2],'D3':board[0][3], 'E3':board[0][4],'F3':board[0][5],'G3':board[0][6],'H3':board[0][7]},
notation_dict_row_two : {'A2':board[1][0],'B2':board[1][1],'C2':board[1][2],'D2':board[1][3], 'E2':board[1][4],'F2':board[1][5],'G2':board[1][6],'H2':board[1][7]},
notation_dict_row_one : {'A1':board[2][0],'B1':board[2][1],'C1':board[2][2],'D1':board[2][3],'E1':board[2][4],'F1':board[2][5],'G1':board[2][6],'H1':board[2][7]}


}'''



    
def row_maker(row,notation_number):
    not_num = 0
    emptystr = ""
    for item in row:
        not_num + 1
        emptystr += row[item] + '  '    
    return emptystr
    
    
def notation(notation_list,notation_number):
    count = 8
    for row in notation_list:
        x = row_maker(row, notation_number)
        print(str(count) + '  ', x)
        count -= 1
    print('\n' + notation_letter)


def give_board():
    notation(notation_list, notation_number)


def user_input(notation_list, playerInput):
    count = 0
    for row_dict in notation_list:
        for key, val in row_dict.items():
            count += 1
            print(key)
            if playerInput == key:
                print('match!')
                return playerInput
            elif playerInput != key:
                print('no match')
                if count <= 64:
                    continue
                elif count > 64:
                    inval = 'invalid'
                    return inval

give_board()
#====================================================================================NOW BEGIN TAKING USER INPUT
while True:
    player_one = input('Player 1: ') 
    try:
        a = user_input(notation_list, player_one)
        print(a)
        if a == player_one:
            break
    except:
        print('invalid input')
        continue
        

'''get user input see if user input contains any dictionary key from any row, if so, move piece, if nay, ask again.'''

'''get correct player input is working, but exceptions are not being handled - they are being treated as correct.'''



#Player_two = input('Player 2:  ')