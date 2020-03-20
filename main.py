import Question
import random

answers = []
selection = []

for i in range(100):
    answers.append(str(i) + " Antwort")

    

selection.append(random.choice(answers))
selection.append(random.choice(answers))
selection.append(random.choice(answers))
selection.append(random.choice(answers))



print(selection)