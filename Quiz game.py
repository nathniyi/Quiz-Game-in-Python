print("Welcome to My Quiz")

playing = input("Do you want to play my quiz? Yes/No: ")

if playing.lower() != "yes":
            quit()

print("Welcome! Lets ramble :) ")
score = 0

Answer = input("What's the biggest animal in the world? ")
if Answer.lower() == "blue whale":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("Who is the current president of USA? ")
if Answer.lower() == "joe biden":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("What is the capital of China? ")
if Answer.lower() == "beijing":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("What does IPO stand for? ")
if Answer.lower() == "initial public offering":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("What planet is closest to the sun? ")
if Answer.lower() == "mercury":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("What is the name of the school in sex education? ")
if Answer.lower() == "moordale high":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

Answer = input("What is the sense of taste? ")
if Answer.lower() == "tongue":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got", score, "questions correctly")
print('you got ' + str((score / 7) * 100) + '%')

