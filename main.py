import csv
import math
import string

# Functions
allowed = 'abcdefghijklmnopqrstuvwxyz1234567890'

def check(x):
    for i in (len(x)):
        if x[i] in allowed:
            return True
    return False


# Reads the ascii art title from greeting.txt
# then prints it to the shell
with open('txt/greeting.txt', 'r') as f:
    print(f.read())

# Defining lists and variables
txt = []
ans = []
phr = ["You might wanna study up a bit", "Good Attempt!", "Almost there!", "So close!", "You did it!! :)"]
userScore = 0

# Reads the questions and answers from questions.tsv 
# then converts them into two separate lists
with open('tsv/questions.tsv', 'r') as file:
    
    # Reads from the .tsv
    tsvFile = csv.reader(file, delimiter="\t") 

    # Adds the variables from the .tsv and converts them into lists
    for line in tsvFile:
        txt.append(line[0]) # Adds the questions to a list
        ans.append(line[1].lower()) # Adds the answers to a list

# Main loop
while True:

    # Asks you all of the questions
    for i in range (len(txt)):

        while True:
            
            # Prints the question and creates an input field
            print("Question {}. {}:".format(i+1, txt[i]))
            userAns = str(input(": ")).lower()

            # Adds score and prints "correct" if you got the question correct,
            if userAns == ans[i]:
                print("Correct! ;)\n")
                userScore += 1
                break
            # Tests if the user enters an invalid input
            elif check(userAns):
                print("It's not a trick question, enter some text\n")
            # Prints "Incorrect" if you got the question wrong
            else:
                print("Incorrect :(\n")
                break

    # Prints out the users results from the quiz
    print("\nYour total score was {} out of {}\n".format(userScore, len(txt))) # Prints the user's score out of x
    userPercent = round(userScore/len(txt)*100) # Works out the user's percentage
    print("That's {}%\n".format(userPercent)) # Prints the user's percentage
    print(phr[math.floor( (len(phr)-1)/100*userPercent )] + "\n") # Prints an appropriate message from the list phr, bases on the user's score

    # Asks the user if they want to go again
    # If the user doesn't want to go again it exits the program
    goAgain = "" # Resets the go again input
    while goAgain != "yes" and goAgain != "y":

        print("\nWould you like to go again? (y/n)")
        goAgain = str(input(": ")).lower()

        if goAgain == "no" or goAgain == "n":
            print("Bye bye!\n\n")
            exit()
            
        print("Invalid input!")

    print("\n\n")

    # Resets the users score
    userScore = 0

    import string