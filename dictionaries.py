# info ={
# "key" : "value",
# "name" : "abdul" ,
# "Qualification" : "BSCS",
# "subject":["phy","math", "chem"],
# "marks":(99.9,223,54,65),
# "age": 26,
# "CGPA" :3.47,
# "is_Adult": True


# }

# info["name"]= "shakoor"
# info["surname"]="abdul8782"
# print(info["name"])
# print(info)


# empty_dic ={}
# empty_dic["key"]= "value"
# print(empty_dic)

# nested_dic ={
#     "key" : "value",
#     "marks":{
#         "urdu" : 55,
#         "math" : 76,
#         "phy" : 74,
#         },
#     "name" : "abdul",
#     "location": "lahore"
# }
# print(type(nested_dic))
# print(nested_dic["marks"]["urdu"])
# print(nested_dic.keys())
# print(len(list(nested_dic.keys())))


# collect ={1,2,3,4, "hello","hello", "world","world"}
# print(collect)
# print(type(collect))


# subjects = { "java","javascript" , "C++", "node" "java", "javascript" ,"C++"}
# print(len(subjects))

subjects = {}
subjects["java"] =75
print(subjects)
print(subjects.keys())
print(subjects.values())
X= int(input("enter your marks of math"))
subjects.update({"math":X})

X= int(input("enter your marks of chem"))
subjects.update({"chem":X})

X= int(input("enter your marks of phy"))
subjects.update({"phy":X})
print(subjects)