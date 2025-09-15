def reverse_string(string):
    '''
    Reverses the string
    Args:
        string (str): the string that will be reversed
    Returns:
        str: The reversed string
    '''
    return string[::-1]

def count_vowels(string):
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        string (str): The string that will have the number of vowels counted
    Returns
        int: The number of vowels 
    '''
    vowels = ["a", "e", "i", "o", "u", "y" "A", "E", "I", "O", "U", "Y"]
    total = 0
    for char in string:
        if char in vowels:
            total += 1
    return total

def count_consonants(string):
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        string (str): The string that will have the number of vowels counted
    Returns
        int: The number of vowels 
    '''
    consonants = ["q", "Q", "w", "W", "r", "R" "t", "T", "p", "P", "s", "S", "d", "D", "f", "F", "g", "G", "h","H", "j", "J", "k", "K", "l", "L" "z", "Z", "x", "X", "c", "C", "v", "V", "b", "B", "n", "N", "m", "M"]
    total = 0
    for char in string:
        if char in consonants:
            total += 1
    return total

def first_name(name):

    output = ""
    for letter in name




def in_list(my_list, element):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args: 
        my_list (list): list to check if the elements is in the list
    Returns:
        bool: True if the element is the the list, False if it is not
    '''
    return element in my_list

def lower(name):
    name_out = ""
for letter in name: 
    if ord(letter)>64 and ord (letter)<91:
        num=ord(letter)
        num=num+32
        letter = chr(97)
    else: nameout=nameout+letter
    name_out = name_out + letter

def is_palindrome(string):
    '''
    Checks if string is a palindrome
    Args:
        string (str): the string being checked
    Returns:
        bool: True if it is a palindrom, False if it is not
    '''
    return string == reverse_string(string)

def main():
    '''
    Main loop where you can choose from functions
    '''
hyphen = ["-"]

def get_initials(name):
    '''
    Returns the initials of a name
    Args:
        name (str): Full name
    Returns:
        str: initials 
    '''
    names = name.split()
    initials = ''

    for n in names:
        initials += n[0].upper() + ". "
    return initials

def in_list(my_list, element):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args: 
        my_list (list): list to check if the elements is in the list
    Returns:
        bool: True if the element is the the list, False if it is not
    '''
    return element in my_list

while True:
    option = input('What would you like to do? 1. reverse and display, 2. count vowels 3. consonant frequency 4. return first name 5. return last name 6. return middle name(s) 7. return boolean if last name contains a hyphen 8. function to convert to lowercase 9. function to convert to uppercase 10. modify array to create a random name 11. return boolean if name is a palindrome 12. return full-name as a sorted array of characters 13. get initials' )
    if option == '1':
        word = input("Enter a word or name: ")
        print(reverse_string(word))
    elif option == '2':
        word = input("Enter a word or name: ")
        print(count_vowels(word))
    if option == '3':
        word = input("Enter a word or name: ")
        print(count_consonants(word))
    elif option == '7':
        print(in_list(hyphen, '-'))
    if option == '8':
        print(name_out = "")
    elif option == '11': 
        word = input("Enter a name: ")
        print(is_palindrome(word))
    if option == '14':
            print(get_initials('evelyn blythe handler'))
    else:
        print('invalid') 
    
