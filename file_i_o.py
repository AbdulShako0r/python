#f=open("demo.txt" , "r+")
#f.write("\n i want to write data in my file")
#line1 = f.readline()
#data= f.read()
#rint(data)

#print(line1)
#f.close()


# with open("demo.txt", "r") as f:
#     data=f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#     f.write("hello word")
    
# import os
# os.remove("sample.txt")

# with open("practice.txt", "w") as f:
#     f.write("hello world\nam learning python\nand am a computer scince graduate")

# with open ("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace( "python", "java")
# print(new_data)
# word="learning"
# with open ("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")

# def check_for_word():
#     word="learning"
#     with open ("practice.txt", "r") as f:
#         data = f.read()
#         if(word in data):
#             print("found")
#         else:
#             print("not found")
# check_for_word()

# def check_for_line():
#     word="scince"
#     data=True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print("THE WORD IS IN LINE :", line_no)
#                 return
#             line_no += 1
#     return -1
# check_for_line()
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
   # print(data)
    # num = ""
    # for i in range(len(data)):
    #     if(data[i]== ","):
    #         print(int(num))
    #         num= ""
    #     else:
    #         num += data[i]
    num =data.split(",")
    for val in num:
        if(int(val) % 2 == 0):
            count += 1
print("the even number in list:", count)