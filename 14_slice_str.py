name = "Felix Centeno"

print(name[0:5:1]) # [start:stop:step]

website1 = "http://google.com"
website2 = "http://wikipedia.com"

print(website1[7:-4])# google
print(website2[7:-4])# wikipedia
slice = slice(7,-4,1) # start, stop, step

print(website1[slice]) # google
print(website2[slice]) # wikipedia
reverse_name = name[::-1]
print(reverse_name)# onetneC xileF
