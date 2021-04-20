# First let's outline the question prompts.
questions_prompts = [
    "What colour are apples?\na) Red\nb) Green\nc) Purple\nd) A and B\n\n",
    "What colour are bananas?\na) Orange\nb) Magenta\nc) Teal\nd) Yellow\n\n",
    "What colour are strawberries?\na) Turquoise\nb) Cyan\nc) Red\nd) Blue\n\n"
]

# Because there are two parts to a question (i.e. question itself and answer) we can create a question class.
    # Let's define one now.
class question_class:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    question_class(questions_prompts[0], "d"), # (prompt, answer)
    question_class(questions_prompts[1], "d"),
    question_class(questions_prompts[2], "c"),
]

# Now we need to write a function that will run the quiz (ask user questions and confirm answer correctness).
def run_quiz(questions):
    score = 0 # We also want to track their score. This is globally defined within the function.
    for question in questions: # For each entry (prompt) in the questions list.
        answer = input(question.prompt) # Storing input w/ each second array entry's prompt attribute (acting as question) 
        # in variable answer.
        if answer == question.answer: # If variable answer = respective entry's defined answer in list "questions".
            score += 1 # Add 1 to score and define as new score variable.
    print("You got " + str(score) + " / " + str(len(questions)) + " questions correct.")

# Now we just need to call the function to run the code.
run_quiz(questions)