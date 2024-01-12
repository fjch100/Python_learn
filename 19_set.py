# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"plate", "cup", "bowl"}

for utensil in utensils:
    print(utensil)

# add element to tuple
utensils.add("napkin")
print(utensils) # {'spoon', 'napkin', 'fork', 'knife'}

#remove one item from tuple
utensils.remove("spoon")
print(utensils) # {'fork', 'napkin', 'knife'}

# add the elements of one tuple to another
utensils.update(dishes)
print(utensils) # {'fork', 'napkin', 'plate', 'cup', 'knife', 'bowl'}

# union two tuples into a new one
table = utensils.union(dishes)
print(table) # {'knife', 'bowl', 'napkin', 'plate', 'fork', 'cup'}


utensils = {"fork", "spoon", "knife"}
dishes = {"plate", "cup", "bowl", "knife"}

# tuples differences
print(utensils.difference(dishes)) # {'fork', 'spoon'}
print(utensils.intersection(dishes)) # {'knife'}

# clear a tuple
utensils.clear()
print(utensils) # set()