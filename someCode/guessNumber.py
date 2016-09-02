print("Welcom to Guess number?")

while 1:
    print('Please Input Your Number')
    g = input('Your Number =')
    ynumber = int(g)
    
    if ynumber == 5:
        print("You Got IT")
        break
    elif ynumber >=5:
        print("Too Hight")
    else:
        print("Too Low")
print('Game Over !! Bye Bye')
        
