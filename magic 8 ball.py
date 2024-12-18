import random

responces = ["yes", "most definitly", "maybe", "most likley", "no", "absolutlely not", "possibly", "signs point to yes",]
questionwords = ["is", "how", "who", "am", "when", "why", "which", "what", "where",]
while True:
    question = input ("ask the magic eight ball a question: ")
    if "?" in question and question.split()[0] in questionwords :
        answer = random.choice(responces)
        print ("magic eight ball says: " + answer)
    else:
        print ("Invalid Response!")                                                                                                   
    
