
import random
print('''


███████╗██╗     ██╗██████╗      █████╗      ██████╗ ██████╗ ██╗███╗   ██╗
██╔════╝██║     ██║██╔══██╗    ██╔══██╗    ██╔════╝██╔═══██╗██║████╗  ██║
█████╗  ██║     ██║██████╔╝    ███████║    ██║     ██║   ██║██║██╔██╗ ██║
██╔══╝  ██║     ██║██╔═══╝     ██╔══██║    ██║     ██║   ██║██║██║╚██╗██║
██║     ███████╗██║██║         ██║  ██║    ╚██████╗╚██████╔╝██║██║ ╚████║
╚═╝     ╚══════╝╚═╝╚═╝         ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝



''')

flipcount = 0
headcount = 0
tailcount = 0
tally = {
    "Total Flips":flipcount,
    "Heads":headcount,
    "Tails":tailcount
}
while True:
    coin = random.randint(0,1)
    x=1
    while x == 1:
        try:
            usertoggle = input('Press the Enter to flip a coin')
            break
        except:
            print('Press Enter')
            continue
    if coin == 1:
        print('Heads!')
        flipcount += 1
        headcount += 1
        tally.update({'Total Flips':flipcount})
        tally.update({'Heads':headcount})
        print(tally)
        continue
    elif coin == 0:
        print('Tails')
        flipcount += 1
        tailcount += 1
        tally.update({'Total Flips':flipcount})       
        tally.update({'Tails':tailcount})
        print(tally)
        continue