#no dollar signs, commas, or periods (I'm not that good yet)
monies = input('How much do you make? Amount: ')
dollas = int(monies)

def buttrape():    
    if dollas < 50000:
        print("You broke ass")
    elif dollas < 80000:
        tax = dollas * .3
        print(f'You owe ${tax} dollas')
    else:
        tax = dollas * .5
        print(f'You are so rich, and owe ${tax}')

buttrape()