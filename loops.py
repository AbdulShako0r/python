# count=1


# while count<=5:
    
#     print("hello world")
#     count +=1
# count =1
# while count <=100:
#     print(count)
#     count +=1
#     i =100
# while i >=1:
#     print(i)
#     i -=1
# num=int(input("Enter a number for multiplication :"))
# count=1
# num=int(input("Enter a number for multiplication :"))

# while count <=10:
    
#     print(num*count)
#     count +=1
#List
# nums=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx< len(nums):
#     print(nums[idx])
#     idx +=1


#Tupple
# nums=(1,4,9,16,25,36,49,64,81,100)
# x=49
# idx=0
# while idx< len(nums):
#     if(nums[idx]==x):
#         print("found")
        
#         print("index :",idx, "where number found",x)
#         break
#    # print(nums[idx])
#     idx +=1

# i=1
# while i<=10:
#     if(i%2==0):
#         i +=1
#         continue
#     print(i)
#     i +=1


#For LOop
# element=[1,3,5,7,9,11,13,15,17,19]

# for val in element:
#     print(val)
# str="abdulshakoor"
# for val in str:
#     print(val)

# nums=[1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)
# element=(1,4,9,16,25,36,49,64,81,100)
# x=25
# for el in element:
#     if(element[el]==x):
#         print("number found at index", el)
#         break
    
# seq=range(10)
# for i in seq:
#     print(i)

# seq=range(0, 10,3)
# for i in seq:
#     print(i)


# for i in range(0, 30,3):
#     print(i)

# for i in range(100, 1, -3):
#     print(i) 


# num= int(input("enter a number: "))
# for i in range(1 , 11):
#     print(i*num)

num= int(input("enter a number: "))
sum=0
for i in range(1, num+1):
    sum +=i
print("total sum is:", sum)


nums= int(input("enter a number: "))
fact=1
for i in range(1, num+1):
    fact *=i
print("total factorial is:", fact)