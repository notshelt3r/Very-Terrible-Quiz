print("Welcome To My Quiz")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Okay! Let's play :D")
score = 0

answer = input("When did Python launch? ")
if answer == "1991":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("Who created Python? ")
if answer == "Guido Van Rossum":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("Who created the first programming language? ")
if answer == "Ada Lovelace":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
    
answer = input("Who created linux? ")
if answer == "Linus Torvalds":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%" + " Correct! ")


