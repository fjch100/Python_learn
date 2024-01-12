""" List methods:
     1. append(object)
     2. extend(list)
     3. insert(index, object)
     4. pop()
     5. remove(item)
     6. sort([key], reverse=False)
     7. clear()
"""
lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
print(lenguajes)
lenguajes[1] = "GO"
print(lenguajes)
print(lenguajes[-3]) # "PHP"
print(lenguajes[1:3]) # ['GO', 'PHP']
print(lenguajes[:3]) # ['Python', 'GO', 'PHP']
print(lenguajes[1:]) # ['GO', 'PHP', 'Javascript', 'Java']
# pop the last element
print(lenguajes.pop())# "Java" 
print(lenguajes)# ['Python', 'GO', 'PHP', 'Javascript']
# Append a elements at list end
lenguajes.append("C++") # append to the end  of list
print(lenguajes)# ['Python', 'GO', 'PHP', 'Javascript', 'C++']
# remove an element by its value
lenguajes.remove("Python")
print(lenguajes)# ['GO', 'PHP', 'Javascript', 'C++']
# insert an element at any position
lenguajes.insert(2,"Rust")# insert(position, value)
print(lenguajes)# ['GO', 'PHP', 'Rust', 'Javascript', 'C++']
# sort list
lenguajes.sort()
print(lenguajes)# ['C++', 'GO', 'Javascript', 'PHP', 'Rust']
# extend
lenguajes.extend(["Cobol"])
print(lenguajes)# ['C++', 'GO', 'Javascript', 'PHP', 'Rust', 'Cobol']
lenguajes.extend("Cobol")
print(lenguajes)# ['C++', 'GO', 'Javascript', 'PHP', 'Rust', 'Cobol', 'C', 'o', 'b', 'o', 'l']
#clear the list
lenguajes.clear()
