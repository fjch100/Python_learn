# tuple = collection witch is ordered and unchangeable
#         used to group together related data

# create a student tuple with name, age, gender
student = ("Bob", 21, "male")
print( student.count("Bob")) # 1, how many "Bob" are there
print( student.index("male"))# 2, index of "male" element

# loop over student elements
for x in student:
    print(x)

# check if an element is in the tuple
if "Bob" in student:
    print("Bob is here")
