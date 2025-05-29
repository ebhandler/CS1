'''Evelyn Handler, foodomatic, 4/4/25, all challenges'''



import random
foods = ["steak", "pasta", "soup", "chicken parm", "pizza", "salmon", "shushi", "salad", "sandwich"]
prices = [60, 40, 30, 50, 45, 55, 65, 25, 35]
flairs = ["potatos", "bread", "crackers", "green beans", "garlic knots", "spinich", "soy sauce", "dressing", "fries"]
flair_prices = [10, 8, 3, 2, 7, 5, 1, 2, 15]                                                 

while True:                                                                                  #forever loop
    game = input ("which game?: rock, paper, scissors, knife or foodomatic ")                #ask which game 

    if game == "foodomatic":                                                                 #if user enters foodomatic
        try:                                                                                 #attempt 
            num_of_items = int(input('how many items do you want? '))                        #ask how many items 
        except ValueError:                                                                   #if user enters somthing else 
            print("enter an intiger value")                                                  #ask user to enter an intiger value 
            continue                                                                         #keep playing
        
        total = 0                                                                            #total is zero
        used = []                                                                            
        
        for i in range(num_of_items):                                                        #repaeat for the number of items 
            food = random.choice(foods)                                                      #food is any from list of foods
            flair = random.choice(flairs)                                                     #flair is any from list of flairs

            if foods+flairs in used:                                                         #if there is a food and a flair used 
                continue                                                                     #keep playing
            used.append(food+flair)                                                          #add to list
            price = prices[foods.index(food)]                                                #price is the price for the food
            flair_price = flair_prices[flairs.index(flair)]                                  #price is the price for the flair
            total += price + flair_price                                                     #total is the price of food and the price of flair
            print (f'{food} with {flair}, ${price+flair_price}')                             #print price of food and flair 
        print(total)                                                                         #print price combined

    elif game == "rock, paper, scissors, knife":                                             #if user plays rock, paper, scissors, knife
        score = 0                                                                            #set score to zero
        options = ['rock', 'paper', 'scissors', 'knife',]                                    #list of options                      
        score_limit = 5                                                                      #set score limit to five

        while True:                                                                          #forever loop
            user = input ("pick a option: Rock, Paper, knife or Scissors: ")                 #user pick rock, paper, or scissores                               
            computer = random.choice(options)                                                #compter randomly chooses rock, paper, or scissors
        
            print(f"user chose {user} and bot chose {computer}")                             #display what user and what bot choose                                          
            if user == "quit":                                                               #is user chooses to quit
                print("bye!")                                                                #display message "bye"
                break                                                                        #ends forever loop
            elif user == computer:                                                           #is users choice is the same as computers choice
                print ("tie")                                                                #there is a tie
            elif user == "rock" and computer == "paper":                                     #if user chooses rock and computer chooses paper
                print("you lost")                                                            #user looses
                score -= 1                                                                   #user looses a point
            elif user == "rock" and computer == "scissors":                                  #if user chooses rock and computer chooses scissors
                print("you won")                                                             #user wins
                score += 1                                                                   #user gains a point
            elif user == "paper" and computer == "scissors":                                 #if user chooses paper and computer chooses scissors
                print("you lost")                                                            #user looses
                score -= 1                                                                   #user looses a point
            elif user == "paper" and computer == "rock":                                     #if user chooses paper and computer chooses rock
                print("you won")                                                             #user wins
                score += 1                                                                   #user gains a point
            elif user == "scissors" and computer == "rock":                                  #if user chooses scissors and computer chooses rock
                print("you lost")                                                            #you lost
                score -= 1                                                                   #user looses a point
            elif user == "scissors" and computer == "paper":                                 #if user chooses scissors and computer chooses paper
                print("you won")                                                             #user wins
                score += 1                                                                   #user gains a point
            elif user == "rock" and computer == "knife":                                     #if user chooses rock and computer chooses knife
                print("you won")                                                             #user wins
                score += 1                                                                   #user gains a point
            elif user == "paper" and computer == "knife":                                    #if user chooses paper and computer chooses knife
                print("you lost")                                                            #user losses
                score -= 1                                                                   #user looses a point
            elif user == "scissors" and computer == "knife":                                 #if user chooses scissors and computer chooses knife
                print("you lost")                                                            #user looses
                score -= 1                                                                   #user looses a point
            elif user == "knife" and computer == "rock":                                     #if user chooses knife and computer chooses rock
                print("you lost")                                                            #user looses
                score -= 1                                                                   #user looses a point
            elif user == "knife" and computer == "paper":                                    #if user chooses knife and computer chooses paper
                print("you won")                                                             #user wins
                score += 1                                                                   #user gains a point
            elif user == "knife" and computer == "scissors":                                 #if user chooses knife and computer chooses scissors
                print("you won")                                                             #user wins
                score += 1                                                                   #user gains a point
            print ("your score is", score)
                                                                                    
    

    
    
    


    
    
        
        


