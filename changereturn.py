import random
print('''

                                                         ▄▄                                             
  ▄▄█▀▀▀█▄█                                            ▀███      ▄█▀▀▀█▄█ ██                            
▄██▀     ▀█                                              ██     ▄██    ▀█ ██                            
██▀       ▀  ▄▄█▀██▀████████▄   ▄▄█▀██▀███▄███ ▄█▀██▄    ██     ▀███▄   ██████  ▄██▀██▄▀███▄███  ▄▄█▀██ 
██          ▄█▀   ██ ██    ██  ▄█▀   ██ ██▀ ▀▀██   ██    ██       ▀█████▄ ██   ██▀   ▀██ ██▀ ▀▀ ▄█▀   ██
██▄    ▀██████▀▀▀▀▀▀ ██    ██  ██▀▀▀▀▀▀ ██     ▄█████    ██     ▄     ▀██ ██   ██     ██ ██     ██▀▀▀▀▀▀
▀██▄     ██ ██▄    ▄ ██    ██  ██▄    ▄ ██    ██   ██    ██     ██     ██ ██   ██▄   ▄██ ██     ██▄    ▄
  ▀▀███████  ▀█████▀████  ████▄ ▀█████▀████▄  ▀████▀██▄▄████▄   █▀█████▀  ▀████ ▀█████▀▄████▄    ▀█████▀
                                                                                                        
  =============================-----------------------------------------=================================                                                                                                      
                                Specializing in warez of dubious quality

''')



i = 1
while i == 1:
    price = random.randrange(1, 1000)
    prompt = ('An item costs: ${}')
    print(prompt.format(price))
    i += 1

while True:
    try:    
        userpay = int((input('Pay me: $')))
        if userpay > price:
            change_returned = userpay-price
            surplusprompt = "Thank you. Your change is ${}"
            print(surplusprompt.format(change_returned))
            break
        elif userpay < price:
            while userpay < price:
                change_returned = price-userpay
                shortprompt = "Bruh. You owe me ${}"
                print(shortprompt.format(change_returned))
                kic = int(input('keep it coming: $'))
                userpay = userpay + kic
                if userpay == price:
                    break
                else:
                    continue
            print('Ah. The classic piecewise payee. Fuck you! Leave my store :)')
            break
        elif userpay == price:
            change_returned = userpay-price
            print('Thank you! Come again :)')
            break
    except:
        print('We only accept money')
