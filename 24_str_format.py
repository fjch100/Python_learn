# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

print("the "+ animal + " jump over the "+ item) # the cow jump over the moon

print("the {} jump over the {}".format(animal, item)) # the cow jump over the moon
print("the {0} jump over the {1}".format(animal, item)) # POSITIONAL ARGUMENT, the cow jump over the moon
print("the {1} jump over the {0}".format(animal, item)) # POSITIONAL ARGUMENT, the moon jump over the cow
print("the {animal2} jump over the {item2}".format(animal2="dog", item2="fence")) # KEYWORD ARGUMENT, the dog jump over the fence

text = "the {} jump over the {}"
print(text.format(animal, item)) # the cow jump over the moon


