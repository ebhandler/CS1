import time
import csv
import os
import random

def enter_keeper(password, tries):
    '''
    Prompts the user to enter a password to enter password keeper.
    Args:
        password (str): secret code to enter password keeper
        tries (int): number of attempts 
    Returns:
        bool: True if login is successful
    '''
    for i in range(tries):
        check_password = input("enter your password for passwordkeeper: ")

        if check_password == password:
            print("Welcome to passwordkeeper!")
            time.sleep(1)
            return True
        else:
            print("wrong password")
    print('Access denied')
    time.sleep(1)
    return False
def add_entry(websites, usernames, passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords.
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
    website = input('enter a website ')
    username = input('enter a username ')
    password = input('enter a password (enter "g" to generate a random password) ')

    if password.lower() == "g":
        password = generate_secure_password()
    websites.append(website)
    usernames.append(username)
    passwords.append(password)
def print_entry(website, username, password):
    '''
    Takes three elements and prints them neatly in an f-string.
    Args:
        website (str): the name of the website
        username (str): the username for the website 
        password (str): the password for the website
    Returns: 
        print: website name, the username, and the password
    '''
    print(f'''
website: {website}
username: {username}
password: {password}
''')
def get_index(websites):
    '''
    Gets the index of the given websites in website.
    Args:
        websites (list): the list of websites
    Returns:
        int: index of the given website
    '''
    while True:
        website = input('enter a website')
        
        if website in websites:
            return websites.index(website)                                                  #returns the index of the given website
        else:
           print('thats not here')
def change_entry(websites, usernames, passwords):
    '''
    Changes usernames and passwords.
    Args:
        websites (list): list of websites
        passwords (list): list of passwords
        usernames (list): list of usernames
    '''
    index = get_index(websites)
    usernames[index] = input(f'Enter your new username for {websites[index]}: ')            #updates the username 
    passwords[index] = input(f'Enter your new password for {websites[index]}: ')            #updates the password
def delete_entry(websites, usernames, passwords):
    '''
    Deletes an entry
    Args:
        websites (list): list of websites
        passwords (list): list of passwords
        usernames (list): list of usernames
    '''
    index = get_index(websites)
    websites.pop(index)                                                                     #removes the website at the specified index
    usernames.pop(index)                                                                    #removes the username at the specified index
    passwords.pop(index)                                                                    #removes the password at the specified index
def get_password_length():
    '''
    Asks user for a desired password length and checks if input is an integer.
    Args:
        None
    Returns:
        int: desired length for password
    '''
    while True:
        try:                                                        #tries to get an integer
            length = int(input('Enter desired password length: '))  #asks the user for the desired password length 
            
            if length < 4:
                print('Please enter a length of at least 4')
                continue
            return length
        except ValueError:                                          #makes sure users input is an integer
            print('Enter an integer')
def password_complexity(password, length, display):
    '''
    Checks how complex/secure passwords are.  
    Args:
        password (str): the password to check
        length (int): the desired password length
        display (bool): to print or not to print a security message
    Returns:
        bool: True/False based on security of password
    '''
    if len(password) < length or password.lower() == password or password.upper() == password or not any(char in password for char in list('`~!@#$%^&*()_+-=?')) or not any(char.isdigit() for char in password): 
        if display:
            print(f'The password {password} is insecure') 
        return False
    else: 
        if display:
            print(f'The password {password} is secure') 
        return True
def generate_secure_password():
    '''
    Generates a secure password for the user.
    Args:
        None
    Returns:
        str: secure password 
    '''
    length = get_password_length()

    while True:
        pwd = ''.join(random.sample(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()_+-=?'), length))  #generates a random secure password 

        if password_complexity(pwd, length, False):
            print(f'Your generated password is {pwd}')
            return pwd
def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.
    Args:
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    if not arrays:
        raise ValueError("At least one array must be provided.")           #make sure the user gave at least one list
    
    num_rows = len(arrays[0])                                              #get number of items from the first list

    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")      #makes sure all lists are the same length
    
    with open(filename, 'w', newline='') as csvfile:                       #open a file 
        csvwriter = csv.writer(csvfile)                                    #makes a csv writer 
        csvwriter.writerow(headers)                                        #writes the headers 

        for i in range(num_rows):
            row = [arr[i] for arr in arrays]                               #takes one row from the lists 
            csvwriter.writerow(row)                                        #writes the row in the file 
def main():
    websites = []
    usernames = []
    passwords = []

    add_entry(websites, usernames, passwords)

    secret_code = input('Enter the code to your password keeper: ')
    time.sleep(1)
    os.system('cls')

    if not enter_keeper(secret_code, 5):
        exit()    
    time.sleep(1)
    os.system('cls')

    while True:
        option = input('''What do you want to do? (Enter "q" to quit):
1. Add another entry
2. Print entry
3. Print all entries 
4. Change an entry
5. Delete an entry
6. Enter a password manually or check a website 
7. Generate password 
8. Store the list of websites with usernames and passwords in an excel spreadsheet                   
        ''').lower()

        if option == "q":
            break
        elif option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif option == "3":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif option == "4":
            change_entry(websites, usernames, passwords)
        elif option == "5":
            delete_entry(websites, usernames, passwords)
        elif option == "6":
            pwd_access = input('Would you like to enter a password manually (m) or check a website (w) ').lower()

            if pwd_access == "m":
                password = input('Enter password: ')
            else:
                index = get_index(websites)
                password = passwords[index]
            length = get_password_length()
            password_complexity(password, length, True)
        elif option == "7":
            pwd = generate_secure_password()
            change_pwd = input('Would you like to change a specific password to this one? y/n ').lower()

            if change_pwd == "y":
                index = get_index(websites)
                passwords[index] = pwd
        elif option == "8":
            filename = input('Enter a file name: ')
            export_to_csv(filename + ".csv", ["Website", "Username", "Password"], websites, usernames, passwords)               #saves websites, usernames, and passwords to .csv 
            print(f'Export successful! Your data has been saved in {filename}.csv')
        else:
            print('invalid')
main()