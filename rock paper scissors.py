#cat
import random 
options = ['rock', 'paper', 'scissors', 'knife',] 
score_limit = 5  

while True:
    game = input("wich game would you like to play. rock, paper, scissors, knife or magic 8 ball: ") #what game do you want to play?
    if game == "rock, paper, scissors, knife": #if user picks rock, paper, scissors, knife
        p1_score = 0 #set playes ones score to 0
        p2_score = 0 #set player two score to 0

        multiplayer = input("do you want to play agaist bot or player?: ") #do you want to play agaist bot or player?
        p1_name = input("whats your name player 1? ") #what is player ones name?
        
        if multiplayer == "bot": #if user chooses to play bot
            p2_name = "bot" #player two name is bot
        elif multiplayer == "player": #if user chooses to play player
            p1_name = input("whats your name player 1? ") #what is player one name?
            p2_name = input("whats your name player 2? ") #what is player two name?
        else: #if user inputs somthing else 
            print("invalid") #display message invalid
            continue
        
        while p1_score < score_limit and p2_score < score_limit: #both player have a score limit
            p1 = input ("pick a option: Rock, Paper, knife or Scissors: ") #user pick rock, paper, or scissores                               

            if multiplayer == "bot": #if user plays bot
                p2 = random.choice(options) #bot randomly chooses rock, paper, or scissors
            else: #if user plays another player
                print("\n"*45) #enter 45 times
                p2 = input ("pick a option: Rock, Paper, knife or Scissors: ") #user pick rock, paper, or scissores   

            print("user chose {p1} and bot chose {p2}") #print was each player chooses                                           
            if p1 == "quit": #if user chooses to quit
                print("bye!") #display message "bye"
                break #ends forever loop
            elif p1 == p2: #if player one choice is the same as player two choice
                print("tie") #there is a tie
            elif p1 == "rock" and p2 == "paper": #if player one chooses rock and player two chooses paper
                print(f"{p2_name} beats {p1_name}.")  #player 1 beats player 2 
                p1_score -= 1 #player one looses a point
                p2_score += 1 #player two gains a point
            elif p1 == "rock" and p2 == "scissors": #if player one chooses rock and player two chooses scissors
                print("{p1_name} beats {p2_name}.") #player 1 beats player 2 
                p1_score += 1 #player one gains a point                                                                   
                p2_score -= 1 #player two looses a point                                                           
            elif p1 == "paper" and p2 == "scissors": #if player one chooses paper and player two chooses sissors 
                print(f"{p2_name} beats {p1_name}.") #player 2 beats player 1 
                p1_score -= 1 #player one looses a point                                                                 
                p2_score += 1 #player two gains a point                                                                
            elif p1 == "paper" and p2 == "rock": #if player one chooses paper and player two chooses rock
                print(f"{p1_name} beats {p2_name}.") #player 1 beats player 2                                                             
                p1_score += 1   #player one gains a point                                                                
                p2_score -= 1   #player two looses a point                                                                 
            elif p1 == "scissors" and p2 == "rock": #if player one chooses rock and player two chooses paper
                print(f"{p2_name} beats {p1_name}.") #player 2 beats player 1                                                            
                p1_score -= 1 #player one looses a point                                                                 
                p2_score += 1 #player two gains a point                                                                 
            elif p1 == "scissors" and p2 == "paper": #if player one chooses scissors and player two chooses paper                             
                print(f"{p1_name} beats {p2_name}.") #player 1 beats player 2                                                           
                p1_score += 1  #player one gains a point                                                                
                p2_score -= 1  #player two looses a point                                                                
            elif p1 == "rock" and p2 == "knife": #if player one chooses rock and player two chooses knife                                      
                print(f"{p1_name} beats {p2_name}.") #player 1 beats player 2                                                             
                p1_score += 1  #player one gains a point                                                                  
                p2_score -= 1  #player two looses a point                                                                  
            elif p1 == "paper" and p2 == "knife": #if player one chooses paper and player two chooses knife                                     
                print(f"{p2_name} beats {p1_name}.") #player 2 beats player 1                                                           
                p1_score -= 1 #player one looses a point                                                                
                p2_score += 1 #player two gains a point                                                                
            elif p1 == "scissors" and p2 == "knife": #if player one chooses scissors and player two chooses knife                                    
                print(f"{p2_name} beats {p1_name}.") #player 2 beats player 1                                                            
                p1_score -= 1 #player one looses a point                                                                
                p2_score += 1 #player two gains a point                                                                   
            elif p1 == "knife" and p2 == "rock": #if player one chooses knife and player two chooses rock                                       
                print(f"{p2_name} beats {p1_name}.") #player 2 beats player 1                                                            
                p1_score -= 1  #player one looses a point                                                                
                p2_score += 1  #player two gains a point                                                                
            elif p1 == "knife" and p2 == "paper": #if player one chooses knife and player two chooses paper                                       
                print(f"{p1_name} beats {p2_name}.") #player 1 beats player 2                                                           
                p1_score += 1 #player one gains a point                                                               
                p2_score -= 1 #player two looses a point                                                                     
            elif p1 == "knife" and p2 == "scissors": #if player one chooses knife and player two chooses scissiors                                   
                print(f"{p1_name} beats {p2_name}.") #player 1 beats player 2                                                         
                p1_score += 2 #player one gains a point                                                                
                p2_score -= 1 #player two looses a point                                                                  
            print(f"{p1_name}: {p1_score} - {p2_name}: {p2_score}") #display player ones score and player twos score

    elif game == "magic 8 ball": #if user chooses magic 8 ball                                                            
        responces = ["yes", "most definitly", "maybe", "most likley", "no", "absolutlely not", "possibly", "signs point to yes",] #options for computer to pick from
        question_words = ["is", "are", "how", "who", "am", "when", "why", "which", "what", "where"] #question words for user to pick from 

        while True: #forever loop
            question = input ("ask the magic eight ball a question, enter stop to end: ").lower() #display message ask the magic eight ball a question

            if question == "stop":
                break
            elif "?" in question and question.split()[0] in question_words : #if user adds a question mark and uses a question word from the list
                answer = random.choice(responces) #display one random choice option
                print ("magic eight ball says: " + answer) #display 
            else: #if user inputs somthing else
                print ("Invalid Response!") #display message invalid
    else:
        print("Invalid response")
    

print("""   
                                                       ___
                                                      |_  |
                                                        | |
__                      ____                            | |
\ ````''''----....____.''\   ````''''-------------------| |--.               _____      .-.
 :.                      `-._                           | |   `''-----''''```     ``'|`: :|
  '::.                       `''--..____________________| |                           | : :|
    '::..       ----....._______________________________| |                           | : :|
      `'-::...__________________________________________| |   .-''-..-''`-..-''`-..-''-.  :|
           ```'''---------------------------------------| |--'                         `'-'
                                                        | |
 ______________
||            ||
||            ||
||            ||
||            ||
||____________||
|______________|
 \\############\\
  \\############\\
   \      ____    \   
    \_____\___\____\                                                    
                                                    
""")
        
