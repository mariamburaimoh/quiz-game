from question_model import *
from data import *
from quiz_brain import *

question_bank = []
for key in question_data:
    question = Question(key["text"], key["answer"])
    question_bank.append(question)

Quiz = QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {Quiz.score}/{Quiz.question_number}.")