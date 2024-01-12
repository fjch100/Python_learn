import  time
lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]

for lenguaje in lenguajes:
    print(lenguaje)

for i in range(5):
    print(i) # 0 1 2 3 4

for i in range(1,5):
    print(i) # 1 2 3 4

for i in range(10,15+1):
    print(i) # 10 11 12 13 14 15

for i in range(10,16, 2): # start , stop, step
    print(i) # 10 12 14

for i in "Felix":
    print(i)

for seconds in range(10,0,-1): # Countdown to 0
    print(seconds)
    time.sleep(1)
print("GO NOW")