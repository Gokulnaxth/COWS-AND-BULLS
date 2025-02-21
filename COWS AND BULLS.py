import random
print( "  BULLS AND COWS ")
print( " Its a two digit guessing game ")

SN = str(random.randint(10,99))
chances = 7

while chances > 0:

    gn = input("Enter the Guessing Number :")

    if SN == gn:
        print(" Congradulation!!! You Won ")
        print("The Secret Number is:", SN)
        break
    else:
        bulls = 0
        cows = 0
        if SN[0] == gn[0]:
            bulls += 1
        if SN[1] == gn[1]:
            bulls += 1
        if SN[0] == gn[1]:
            cows += 1
        if SN[1] == gn[0]:
            cows += 1
    print("BULLS:", bulls)
    print("COWS:", cows)

chances -= 1

while chances < 1:
    print("YOU LOST THE GAME")
    print("The Secret Number is :", SN)
    break
