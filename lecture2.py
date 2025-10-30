# #Strings & Conditional Statements
# str= "this is a string. \n and am started learning string today"
# len1= len(str)
# print(len1)
# char=str[2]
# char1=str[5:10]
# char2=str[5:len(str)]
# print(str.endswith("today"))
# print(str.capitalize())
# print(str.replace("i","u"))


# print("3rd characer is ", char)
# print("index characer is ", char1)
# print("complete characer is ", char2)



# str1="\tthis the 2nd string"
# finalstr=str+str1
# print(finalstr)

# str=input("enter your name :")
# print(len(str),str)
# print(str.count("a"))

age=int(input("enter your age: "))
if(age>=18):
    if(age>80):
        print("older citizen")
    else:
        (print("can apply for id card &license"))
    
elif(age<=18 and age >=16):
    print("wait till your age can't be 18")
elif(age <=15):
    print("not mature enough")
else:
    (print("try again"))
# marks=int(input("enter your marks:"))
# if(marks>=90):
#     print("Grade A")
# elif(marks >=80 and marks<=89):
#     print("Grade B")
# elif(marks >=70 and marks<=79):
#     print("Grade c")
# elif(marks >=60 and marks<=69):
#     print("Grade D")
# else:print("Grade F: you need improvement")
# print("code end")