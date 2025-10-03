import random

def reverse_string(string):        
    '''
    Reverses the string
    Args:
        string (str): the string that will be reversed
    Returns:
        str: The reversed string
    '''
    return string[::-1]                         #takes a string and reverses it

def count_vowels(string):     
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        string (str): The string that will have the number of vowels counted
    Returns:
        int: The number of vowels 
    '''
    vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
    total = 0
    for char in string:
        if char in vowels:
            total += 1
    return total                                #counts the vowels 

def count_consonants(string):      
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        string (str): The string that will have the number of vowels counted
    Returns:
        int: The number of vowels 
    '''
    consonants = ["q", "Q", "w", "W", "r", "R", "t", "T", "p", "P", "s", "S", "d", "D", "f", "F", "g", "G", "h","H", "j", "J", "k", "K", "l", "L", "z", "Z", "x", "X", "c", "C", "v", "V", "b", "B", "n", "N", "m", "M"]
    total = 0
    for char in string:
        if char in consonants:
            total += 1
    return total                               #counts the consonants 

def get_names(fullname):       
    '''
    Splits a fullname into first middle and last
    Args:
        fullname (str): The fullname 
    Returns:
        list: list of names
    '''
    names = []
    name = ''
    for (letter) in fullname:
        if letter == " ":
            names.append(name)
            name = ''
        else:
            name += letter
    names.append(name)
    return names                                #gets the fullname 

def first_name(name):      
    '''
    Takes a name and returns the first name 
    Args:
        (str): full name
    Returns:
        (str): first name
    '''
    fullname = get_names(name)
    return fullname[0]                          #returns the first name 
    
def middle_name(name):    
    '''
    Takes a name and returns the middle name 
    Args:
        (str): full name
    Returns:
        (str): middle name
    '''
    fullname = get_names(name)
    return " ".join(fullname[1:-1])              #returns the middle name 
    
def last_name(name):     
    '''
    Takes a name and returns the last name 
    Args:
        (str): full name
    Returns:
        (str): last name
    '''
    fullname = get_names(name)
    return fullname[-1]                           #returns the last name 

def lowercase(name):       
    '''
    Takes a name and converts it to lowercase
    Args: 
        (str): full name
    Returns:
        (str): lowercase name
    '''
    name_out = "" 
    for letter in name:
        if ord(letter) > 64 and ord (letter) < 91:
            num = ord(letter)
            num += 32
            letter = chr(num)
        name_out += letter
    return name_out                                #converts the name to lowercase 

def uppercase(name):      
    '''
    Takes a name and converts it to uppercase
    Args: 
        (str): full name
    Returns:
        (str): uppercase name
    '''
    name_out = ""
    for letter in name:
            if ord(letter) >= 97 and ord(letter) <= 122:
                num = ord(letter)
                num -= 32
                letter = chr(num)
            name_out += letter
    return name_out                                 #converts the name to uppercase 

def is_palindrome(first_name):   
    '''
    Checks if name is a palindrome
    Args:
        string (str): the string being checked
    Returns:
        bool: True if it is a palindrom, False if it is not
    '''
    return reverse_string(first_name) == first_name #returns true or false based on if the name is a palindrome 

def get_initials(name):    
    '''
    Returns the initials of a name
    Args:
        name (str): Full name
    Returns:
        str: initials 
    '''
    names = get_names(name)
    initials = ''

    for n in names:
        initials += uppercase(n[0]) + ". "
    return initials                                 #gets the initials of a name 

def get_title(name):    
    '''
    Determines if a title is in the name
    Args:
        array (list): somthing from the list
        element (any): somthing not in the list
    Returns:
        bool: True/False based on if element is in array
    '''
    titles = ['Dr.', 'Sir', 'Esq', 'Ph.d', 'Rev.']
    for title in titles:
        return title in get_names(name)             #returns true or false based on if the name contains a title 

def hyphen(full_name): 
    '''
    Determines whether the list contains a hypen 
    Args:
        fullname (str): full name
    Returns:
        bool: True/False based on if element is in array
    '''
    return "-" in last_name(full_name)             #return true or false if the name contains a hyphen 
    
def generate_randomname(name):
    '''
    Generates a random name for the user.
    Args:
        None
    Returns:
        str: random nmame 
    '''
    names = get_names(name)
    name = list(first_name(names))
    random.shuffle(name)
    return ''.join(name)                           #generates a random name 

def main():
    '''
    Main loop where you can choose from functions
    '''
    while True:
            name = input("Enter your name: ")
            option = input('What would you like to do? 1. reverse 2. count vowels 3. count consonants 4. first name 5. last name 6. middle name(s) 7. checks for hyphen 8. convert to lowercase 9. convert to uppercase 10. create a random name 11. check if name is a palindrome 12. get initials 13. check for title/distinction: ')
            if option == '1':
                print(reverse_string(name))
            elif option == '2':
                print(count_vowels(name))
            elif option == '3':
                print(count_consonants(name))
            elif option == '4':
                print(first_name(name))
            elif option == '5':
                print(last_name(name))
            elif option == '6':
                print(middle_name(name))
            elif option == '7':
                print(hyphen(name))
            elif option == '8':
                print(lowercase(name))
            elif option == '9':
                print(uppercase(name))
            elif option == '10':
                print(generate_randomname(name))
            elif option == '11': 
                print(is_palindrome(name))
            elif option == '12':
                print(get_initials(name))
            elif option == '13':
                print(get_title(name))
            else:
                print('false') 

main ()
