import time
import random
def chorus():
    '''
    Prints the chorus of a song
    Args:
        None
    Returns:
        print: chorus
    '''
    print("let it grow")
    print("let it grow")

def sing():
    '''
    Print lyrics of Let it Grow
    Args:
        None
    Returns:
        None
    '''
    print("You don't know me, but my name's Cy")
    print("I'm just the O'Hare delivery guy")
    print("But it seems like trees might be worth a try")
    print("So I say, let it grow")
    print("My name is Dan")
    print("And my name's Rose")
    print("Our son Wesley kinda glows")
    print("And that's not good so we suppose")
    print("We should let it grow")
    chorus()
    print("You can't reap what you don't sow")
    print("Plant the seed inside the earth")
    print("Just one way to know it's worth")
    print("Let's celebrate the world's rebirth")
    print("We say let it grow")
    print("My name's Marie")
    print("And I am three!")
    print("I would really like to see a tree")
    print("La-la-la-la, la, la-la, lee")
    print("I say let it grow")
    print("I'm Grammy Norma")
    print("I'm old and I've got gray hair")
    print("But I remember when trees were everywhere")
    print("And no one had to pay for air")
    print("So I say, let it grow")
    chorus()
    print("Like it did so long ago")
    print("It is just one tiny seed")
    print("But it's all we really need")
    print("It's time to change your life we lead")
    print("Time to let it grow")
    print("My name's O'Hare, I'm one of you")
    print("I live here in Thneedville, too")
    print("The things you say just might be true")
    print("It could be time to start anew")
    print("And maybe change my point of view")
    print("Nah! I say let it die")
    print("Let it die, let it die")
    print("Let it shrivel up and")
    print("Come on, who's with me?")
    print("Nobody")
    print("You greedy dirtbag!")
    chorus()
    print("Let the love inside you show")
    print("Plant the seed inside the earth")
    print("Just one way, to know it's worth")
    print("Let's celebrate the world's rebirth")
    print("We say let it grow")
    chorus()
    print("You can't reap what you don't sow")
    print("It's just one tiny seed")
    print("But it's all we really need")
    print("It's time to banish all your greed")
    print("Imagine Thneedville flowered and treed")
    print("Let this be our solemn creed")
    print("We say let it grow, in Thneedville")
    print("We say let it grow, it's a brand new dawn")
    print("We say let it grow, in Thneedville")
    print("We say let it grow, it's a brand new dawn")

def add(a, b):
    '''
    Takes two numbers and adds them together
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: the sum of two numbers
    '''
    print(a + b)
    
def print_list(my_list):
    '''
    Takes a list and prints every element in that list individually
    Args:
        my_list (list): List of elements
    Returns:
        print: element in list
    '''
    for element in my_list:
        print(element)
        
def in_list(my_list, element):
    '''
    Takes a list and element and returns a boolean based on if the element is in the list
    Args: 
        my_list (list): list to check if the elements is in the list
    Returns:
        bool: True if the element is the the list, False if it is not
    '''
    return element in my_list

def is_integer (number):
    '''
    Takes any parameter and returns a boolean based on if it is an integer
    Args:
        number (str): The value that will be checked
    Returns:
        bool: True if it is an integer, False if it is not
    '''
    try:
        int(number)
        return True
    except ValueError:
        return False
    
def get_integers():
    '''
    Asks the user for two numbers, uses is_integer to check input, returns the two integers
    Args:
        None
    Returns:
        The integers from the user 
    '''
    while True:
        number_1 = input("enter a number")
        number_2 = input("enter another number")
        
        if is_integer(number_1) and is_integer(number_2):
            return int(number_1), int(number_2)
        
def get_random():
    '''
    Uses get_integers and prints a random number between the two given integers
    Args:
        None
    Returns:
        None
    '''
    a, b = get_integers()
    print(random.randint(a, b))
    
def count_vowels(string):
    '''
    Takes a string and returns the number of vowels in it 
    Args:
        string (str): The string that will have the number of vowels counted
    Returns
        int: The number of vowels 
    '''
    vowels = ["a", "e", "i", "o", "u", "y"]
    total = 0
    for char in string:
        if char in vowels:
            total += 1
    return total

def reverse_string(string):
    '''
    Reverses the string
    Args:
        string (str): the string that will be reversed
    Returns:
        str: The reversed string
    '''
    return string[::-1]

def is_palindrome(string):
    '''
    Checks if string is a palindrome
    Args:
        string (str): the string being checked
    Returns:
        bool: True if it is a palindrom, False if it is not
    '''
    return string == reverse_string(string)

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

def main():
    '''
    Main loop where you can choose from functions
    '''
    colors = ["Blue", "Brown", "Green", "Yellow", "Red", "Pink", "Cyan"]

    while True:
        option = input('What would you like to do? 1. Sing a song, 2. Add two numbers, 3. Print a list 4. Check if element is on the list 5. Check if something is an integer 6. Print random number between two inegers 7. Count vowels 8. Reverse string 9. Is it a palindrome 10. Get your initials')
        if option == '1':
            sing()
        elif option == '2':
            a, b = get_integers()
            add(a, b)
        elif option == '3':
            print_list(colors)
        elif option == '4':
            print(in_list(colors, 'Blue'))
            print(in_list(colors, 'Black'))
        elif option == '5':
            print(is_integer('hello'))
            print(is_integer('3'))
        elif option == '6':
            get_random()
        elif option == '7':
            word = input("Enter a word: ")
            print(count_vowels(word))
        elif option == '8':
            word = input("Enter a word: ")
            print(reverse_string(word))
        elif option == '9':
            word = input("Enter a word: ")
            print(is_palindrome(word))
        elif option == '10':
            print(get_initials('evelyn blythe handler'))
        else:
            print('invalid')
main()







    
