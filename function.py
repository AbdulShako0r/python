# def cal_sum(a,b):
#     sum= a+b
#     print(sum)
#     return sum
# cal_sum(4,7)


# cal_sum(56,65)


# cal_sum(3424,6756)


# def cal_sum1(a, b):
#     return a+b
# print(cal_sum1(45,32))

# def print_sum():
#     print("Hello world")

# print_sum()


# def avg_func_sum(a,b,c):
#     avg=(a+b+c)/3
#     return avg
# print(avg_func_sum(4,6,8))


# name=["ali", "Ahmed", "shan", "hamza","shakeel","shaweer"]
# cities=["lahore", "multan", "fsd","DG khan"]
# def len_list(list):
#     print(len(list)) 
# len_list(name)
# len_list(cities)

# def print_list(list):
#     for item in list:
#         print(item,end= " ")
# print_list(cities)

# fact=int(input("enter a number to get factorial:"))
# n=5
# def fact_cal(n):
#    fact=1
#    for item in range(1, n+1):
#        fact *=item
#        print(fact)

# nums= int(input("enter a number: "))
# n=5
# def fact_cal(n):
#     fact=1
#     for i in range(1, n+1):
#          fact *= i
#     print("total factorial is:", fact)
# fact_cal(n)
# n= int(input("enter a number: "))

# def fact_cal(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print("Total factorial is:", fact)

# fact_cal(n)

note = int(input("enter some currency to convert :"))
def converter_currency(note):
    change = 287
    change *= note
    print("the amount you enter in USD$ is :" , change)
converter_currency(note)

num = int(input("enter a number "))

def check_number(num):
    if(num % 2 ==0):
        print("even")
    else:(print("ODD"))
check_number(num)