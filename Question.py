import random

class Question:
    def __init__(self, question:str, answer:str, category:str):
        self.question = question
        self.category = category
        self.answer = answer 

    def setChoices(self, choices):
        self.choices = choices

    def giveChoices(self):
        final_answers = self.choices
        final_answers.append(self.answer)

        random.shuffle(final_answers)

        return final_answers

class Answers:

    def __init__(self, answers, category):
        self.answers = answers
        self.category = category

    # die Antworten, die an Question als Auswahlmöglichkeiten gegeben werden
    def getAnswers(self):

        choices = []
        
        choices.append(random.choices(self.answers))
        choices.append(random.choices(self.answers))
        choices.append(random.choices(self.answers))

        random.shuffle(choices)

        return choices


if __name__ == "__main__":

    q = Question("Frage 1", "Antwort 1", "Kat 1")
    a = Answers(["a1","a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"], "kat 1")

    q.setChoices(a.getAnswers())
    print(q.giveChoices())


    # wo ist die quotes csv ??