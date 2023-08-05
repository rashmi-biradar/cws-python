password = input("Please enter a password: ")

# Assign variables to count the occurrences of each criteria
uppercase = 0
lowercase = 0
number = 0
special_character = 0
total = 0

# Define strings of characters for uppercase, lowercase, numbers, and special characters
uppercase_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_characters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*"

# Check the length of the password
if len(password) >= 8:
    for char in password:
        # Check for uppercase
        if char in uppercase_characters:
            uppercase = 1
        # Check for lowercase
        elif char in lowercase_characters:
            lowercase = 1
        # Check for numbers
        elif char in numbers:
            number = 1
        # Check for special characters
        elif char in special_characters:
            special_character = 1
else:
    total = -1
    print("Enter atleast 8 character")

# Calculate the total number of criteria met
# print(uppercase, lowercase, number, special_character)
total = total + uppercase + lowercase + number + special_character

# Determine the password's strength based on the number of criteria met
# print(total)
if total >= 0:
    if total == 4:
        strength = "Strong"
    elif total == 3:
        strength = "Moderate"
    elif total == 1 or total == 2:
        strength = "Weak"
    elif total == 0:
        print("Password does not match with the criteria")
        strength = "Not Eligible"

    # Display the password's strength to the user
    print(f"The password strength is: {strength}")
