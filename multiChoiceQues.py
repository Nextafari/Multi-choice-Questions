class Question(object):
#Initializing the object
    def __init__(self, prompt, answer ):
        self.prompt = prompt
        self.answer = answer

#This is a variable containing some multi-choice questions and their answers
questions = [
    "What colours are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colours are Bananas?\n(a) Teal\n(b) Magenta \n(c) Yellow\n\n",
    "What colours are Mangoes?\n(a) Green/Yellow\n(b) Red\n(c) Orange\n\n"
]

#Here three objects were created and assigned to a variable
question1 = [
    Question(questions[0], "a"),
    Question(questions[1], "c"),
    Question(questions[2], "a")
]

#A function was created and a variable score was set to zero which will later be incremented, a for loop was also 
# initiated to loop through the objects and display the questions in the objects on the terminal, and also to compare 
# a users answer against the answers in the object and increment the score variable

def test_questions(self):
    score = 0
    for i in question1:
        answer = input(i.prompt)
        if answer == i.answer:
            score += 1
    #score was converted to a string here cos it is an integer same as the length of the questions, this is to avoid error messages
    print("You got " + str(score) + "/" + str(len(question1)) + " questions" + " correct")

#when the function is called, it prints the user's score and just as it is in the print statement
test_questions(question1)
