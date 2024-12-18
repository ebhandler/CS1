import time
import datetime

def print_colored_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')  # Default to white if color not found
    print(f"{color_code}{text}\033[0m")  # Print text with color and reset
def input_colored_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',  # Reset to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m')  # Default to white if color not found
    return input(f"{color_code}{text}\033[0m")  # Print text with color and reset

print_colored_text("hello world", 'red')
response = input_colored_text("user input: ", 'blue')
if response == "yes":
    print_colored_text('yay', 'green')

print_colored_text ("Alarm!", 'blue')

while True:
    snooze = str.lower (input ("snooze? y/n:"))
    
    if snooze == "yes":
        print_colored_text  ("Sleep for 5 more miniutes", 'red')
        time.sleep(5)
        print ("Alarm")
    elif snooze == "no":
        break
    else:
        print ("Invalid Response!")
        print ("Get up")

while True:
    do_I_need_to_study = str.lower (input ("Do I need to study yes/no: "))
    if do_I_need_to_study == "yes":
        print_colored_text ("Get dressed quickly", 'cyan')
        print_colored_text ("Study", 'magenta')
        break
        print ("Invalid Response!")
    elif do_I_need_to_study == "no":
        print ("Get dressed")
        break
    else:
        print ("Invalid Response!")

while True:
    am_I_hungry = str.lower (input ("Am I Hungry? yes/no: "))
    if am_I_hungry == "yes":
        print_colored_text ("eat somthing", 'yellow')
        time.sleep(10)
        print_colored_text ("pack backpack", 'green')
        break
        print ("Invalid Response!")
    elif am_I_hungry == "no":
        print ("pack backpack")
        break
    else:
        print ("Invalid Response!")

while True:
    do_I_want_to_bring_water = str.lower (input ("Do I want to bring water yes/no: "))
    if do_I_want_to_bring_water == "yes":
        print_colored_text ("fill water bottle", 'green')
        break
        print ("Invalid Response!")
    elif do_I_want_to_bring_water == "no":
        print ("leave water bottle at home")
        break
    else:
        print ("Invalid Response!")


while True:
    is_it_cold = str.lower (input ("Is it cold? yes/no: "))
    if is_it_cold  == "yes":
        print_colored_text ("Put on a jacket", 'cyan')
        print ("leave for school")
        break
        print ("Invalid Response!")
    elif is_it_cold == "no":
        print_colored_text ("leave for school", 'red')
        break
    else:
        print ("Invalid Response!")
