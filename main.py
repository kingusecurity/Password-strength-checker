import re
from colorama import init, Fore
from datetime import datetime

# Initialize colorama
init()

# Logging function
def write_log(password, strength):

    with open("log.txt", "a") as log_file:

        timestamp = datetime.now()

        log_file.write(
            f"[{timestamp}] Password Checked | Strength: {strength}\n"
        )

# Password checker function
def check_password(password):

    score = 0

    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Symbol check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special symbols")

    # Strength rating
    if score <= 2:
        strength = "Weak"
        color = Fore.RED

    elif score <= 4:
        strength = "Medium"
        color = Fore.YELLOW

    else:
        strength = "Strong"
        color = Fore.GREEN

    return strength, color, feedback

# Main program loop
while True:

    print(Fore.CYAN + "\n=== Password Strength Checker ===")
    print(Fore.YELLOW + "1. Check Password")
    print(Fore.YELLOW + "2. Exit")

    choice = input(Fore.WHITE + "Choose option: ")

    # Check password
    if choice == "1":

        password = input(Fore.WHITE + "Enter password: ")

        strength, color, feedback = check_password(password)

        print(color + f"\nPassword Strength: {strength}")

        if feedback:
            print(Fore.CYAN + "Feedback:")
            for item in feedback:
                print(Fore.WHITE + f" - {item}")

        write_log(password, strength)

    # Exit
    elif choice == "2":

        print(Fore.CYAN + "Goodbye!")
        break

    else:

        print(Fore.RED + "\nInvalid choice!")