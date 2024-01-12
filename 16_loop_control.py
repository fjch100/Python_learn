#Loop Control Statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips the rest of the code inside the loop and jumps to the next iteration
# pass = does nothing, acts as a placeholder

# ******** break ************
while True:
    name = input("Enter your name: ")
    if name != "":
        break

# ******** continue ************
phone_number = "123-456-7890"
for i in phone_number:
    if i=="-":
        continue
    print(i, end="")

# ******** pass ************
for i in range(1,15):
    if i==13:
        pass
    else:
        print(i)