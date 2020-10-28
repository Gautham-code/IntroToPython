import random
 
game = random.randrange(1,10)
print(game)
 
shuffle = int(input("Enter your number:"))
 
if shuffle == hidden:
    print("You are right")
elif shuffle < hidden:
    print("You loose")
else:
    print("You loose")
