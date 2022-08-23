board = [['.  .  .  .  .  .  .  .'],['P  P  P  P  P  P  P  P'],['R  N  B  K  Q  B  N  R']]
notation = ['A  B  C  D  E  F  G  H']  
notation_number = ['1', '2', '3', '4', '5', '6', '7','8']     

for number in notation_number:
    notation_number.reverse()
    if number != '1' and number != '2' and number != '7' and number != '8':
        print(notation_number[int(number) - 1],' ',board[0])
    elif number == '2' or number == '7':
        print(notation_number[int(number) - 1],' ',board[1])
    elif number == '1' or number == '8':
        print(notation_number[int(number) - 1],' ',board[2])

print()
print('   ' , notation)









