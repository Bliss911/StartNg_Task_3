import random

print("************* Welcome to the Modified Guessing game *********************")

print("""
What level of difficulty do you want?
1. Easy
2. Medium
3. Hard

""")
while True:
    difficulty_choice = input("Pick a choice: ")

    if difficulty_choice == "1":
        num = 6
        random_value = random.randint(1, 10)

        print("You have 6 guesses to make\n")
        for attempt in range(num):
            guess = input("Make a guess: ")
            while not guess.isnumeric():
                print("You did not enter a number")
                guess = input("Make a guess: ")
            if int(guess) == int(random_value):
                print("Congratulations! you made a correct guess")
                break
            else:
                num -= 1
                print("Wrong Choice. Try again" + " You have " + str(num) + " attempts remaining\n")

        print("Game over!\n")
        print(f"The random value is: {random_value}")
        break

    elif difficulty_choice == "2":
        num = 4
        random_value = random.randint(1, 20)

        print("You have 4 guesses to make\n")
        for attempt in range(num):
            guess = input("Make a guess: ")
            while not guess.isnumeric():
                print("Enter a number")
                guess = input("Make a guess: ")
            if int(guess) == int(random_value):
                print("Congratulations! you made a correct guess")
                break
            else:
                num -= 1
                print("Wrong guess. Try again" + " You have " + str(num) + " attempts remaining\n")

        print("Game over!\n")
        print(f"The random value is: {random_value}")
        break

    elif difficulty_choice == "3":
        num = 3
        random_value = random.randint(1, 50)

        print("You have 3 guesses to make\n")
        for attempt in range(num):
            guess = input("Make a guess:")
            while not guess.isnumeric():
                print("Enter a number")
                guess = input("Make a guess: ")
            if int(guess) == int(random_value):
                print("Congratulations! you made a correct guess")
                break
            else:
                num -= 1
                print("Wrong guess. Try again" + " You have " + str(num) + " attempts remaining\n")
        print("Game over!\n")
        print(f"The random value is: {random_value}")
        break

    else:
        print("Wrong choice")
        print("Please enter a valid choice and continue")
