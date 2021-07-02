import random

answer = random.randint(0,100)
guesses = 0
game = 1
our_list = []

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, guesses = data.split("|")
            print("Past Scores")
            print("Name:", name, "| Score:", guesses)

while True:
    i = input("Type p to play and  q to quit: ")
    if i == "q":
        break
    else:
        name = input("What's your name? : ")

        guess = int(input("Guess a number 0-100: "))
        if guess == answer:
            game = game+1
            print(f"Congratulation {name} you got it on your first try! Are you cheating?")
            break
        else:
            print(f"Sorry {name} you didn't get it first try but you can still guess again.")
        while game <= 1:
            our_list.append(guess)
            print(f"Past guesses:{our_list}")
            guess = int(input(" Guess: "))

            if guess < answer:
                print("Try guessing higher.")
                guesses = guesses+1
            elif guess > answer:
                print("Try guessing lower.")
                guesses = guesses+1
            else:
                print(f"Congratulations {name} you got it in {guesses + 2} tries!")
                print(f"Answer:{answer}")
                guesses = str(guesses + 2)

                with open("passwords.txt", "a") as f:
                    f.write(name + "|" + (guesses) + "\n")
                game = game+1
                break
view()