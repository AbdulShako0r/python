# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     # fact *= n
#     return fact(n-1) * n
# print(fact(5))

# def sum(n):
#     if(n == 0):
#         return 0
#     return sum(n-1) + n
# print(sum(5))

# cities=["lahore", "multan", "fsd","DG khan"]
# def lenght_list(list, idx):
#     if(idx == len(list)):
#         return
#     print(list(idx))
#     lenght_list(list , idx+1)

# lenght_list(cities)

cities = ["lahore", "multan", "fsd", "DG khan"]

def length_list(lst, idx):
    if idx == len(lst):
        return
    print(lst[idx])
    length_list(lst, idx + 1)

print(length_list(cities, 0))