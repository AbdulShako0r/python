# marks=[20,40,50,70,90]
# print(marks)
# print(marks[-3:-1])
# print(type(marks))

# student= ["abdul" , 26," Lahore"]
# print(student)
# student[0]="shakoor"
# print(student)
# age=[40,30,20,60,45,70,55,43]
# age.insert(2,66)
# age.remove(70)
# age.pop(3)
# age.append(57)
# age.sort()
# print(age.sort(reverse=True))
# print(age)
# movies=[]
# mov1=input("enter the name of 1st movie:")
# mov2=input("enter the name of 2nd movie:")
# mov3=input("enter the name of 3rd movie:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# movies.append(input("enter the name of 4th movie"))
# print(movies)
# copy_movies=movies.copy()
# copy_movies.reverse()
# if(movies==copy_movies):
#     print("same")
# else:
#     print("not same")



#tuples
# tup=(2,3,4,5,64,8,5,7)
# print(type(tup))


randint=range(1, 11)
player1=int(input("enter a number between 1-10"))

while True:
            player2 = int(input("Guess the number (1-10): "))
            if player2 < player1:
                 print("Too low! Try again.")
            elif player2 > player1:
                 print("Too high! Try again.")
            else:
                 print(" You got it! The number was", player2)
                 break