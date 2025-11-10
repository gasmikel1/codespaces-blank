def homework_status(class_work, homework):
    if class_work == 2 and homework == 1:
        return "All assignments completed."
    elif class_work == 2 and homework == 0:
        return "No homework assigned."
    elif class_work == 1 and homework == 1:
        return "Some assignments completed."
    else:
        return "Pending assignments."
    
homework_status(1, 1)


def reversword(word): 
    txt = word[::-1]
    print(txt)
reversword('Mikel')



import random

def guess_the_number():
    """Plays a number guessing game with the user."""
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low! Try guessing higher.")
            elif user_guess > secret_number:
                print("Too high! Try guessing lower.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    guess_the_number()

