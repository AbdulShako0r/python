randint=range(1, 11)
player1=int(input("enter a number between 1-10: "))

while True:
            player2 = int(input("Guess the number (1-10): "))
            if player2 < player1:
                 print("Too low! Try again.")
            elif player2 > player1:
                 print("Too high! Try again.")
            else:
                 print(" You're Right, The number is", player2)
                 break