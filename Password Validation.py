"""Password validation requirements:
- at least 8 characters
- at least 1 lowercase letter
- at least 1 uppercase letter
- at least 1 digit
- store the string to a txt file
Optional:
- include a special character validation
- if password is valid ask user to confirm the password
- allow more than one password to be entered if the user wants to"""

while True:
    # Conditions for the password
    length = False
    up_case = False
    low_case = False
    digit = False
    special = False

    # Takes user input while also informing them about requirements
    user_pw = input('''\nPlease enter a new password
    REQUIREMENTS:
    -At least 8 characters
    -At least 1 uppercase letter
    -At least 1 lowercase letter
    -At least 1 digit
    -At least 1 special character Ex:! @ # $ % ^ & * ( )
    \nNew Password: ''')

    if len(user_pw) >= 8:
        length = True

    # Checks every character in the password and sets the variables to true if the condition is met
    for i in user_pw:

        if i.isupper():
            up_case = True
        elif i.islower():
            low_case = True
        elif i.isdigit():
            digit = True
        elif i.isalnum() is False:
            special = True

    # checks if each condition is met
    if up_case and digit and low_case and length and special is True:
        verify = input('Please enter the password again to verify: ')
        # final verification for the users password
        if verify == user_pw:
            # Asks the user what the pw is for
            use_case = input('What is the password for? ')
            file = open("storedpw.txt", 'a')

            # There's probably an easier way to do this but ¯\_(ツ)_/¯
            file.write(use_case + ':     ')
            file.write(user_pw + '\n')
            file.close()
            print('Password set!!!')

            restart = input('Would you like to enter a new password (y/n)? ')
            if restart != 'y':
                break
        else:
            print('Incorrect, please restart.')
    else:
        print('\nPlease enter a valid password!!!\n')
