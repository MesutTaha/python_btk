class Question:
    def __init__(self, txt, choices, answer):
        self.text = txt
        self.choices = choices
        self.answer = answer
    
    def check_answer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex= 0

    def getQuestionIndex(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestionIndex()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for i in question.choices:
            print('-'+ i)
        
        answer = input('Cevap: ')
        self.calculate_score(answer=answer)
        self.loadquesstion()

    def calculate_score(self, answer):
        question = self.getQuestionIndex()

        if question.check_answer(answer):
            self.score += 1
        self.questionIndex += 1
    
    def loadquesstion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def showScore(self):
        print('Score', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz Bitti')
        else:
            print(f'- Question {questionNumber}/{totalQuestion} -'.center(100,'*'))
    """ def sorular(self):
        while self.questionIndex + 1 <= len(questions):

            self.displayQuestion()
            self.calculate_score()
            #if questions[self.questionIndex].check_answer(self.answer):
            #    self.score += 1
            self.questionIndex += 1
        
        print(self.score) """




q1 = Question('En iyi programlama dili hangisidir?', ['C#', 'Python', 'Java', 'Kotlin'], 'Python')
q2 = Question('En iyi Türk takimi hangisidir?', ['FB', 'BJK', 'TS', 'GS'], 'GS')
q3 = Question('En iyi müzik grubu hangisidir?', ['Duman', 'Gripin', 'Manga', '84'], 'Manga')
q4 = Question('En iyi konsol oyunu hangisidir?', ['GoW', 'Uncharted', 'The Last of Us', 'Ghost of Tsushima'], 'GoW')

questions = [q1, q2, q3, q4]
quiz = Quiz(questions= questions)

""" 
quiz = Quiz(questions= questions)
question = quiz.questions[quiz.questionIndex]

# Yukaridaki kod bloklari Quiz classinin içersindeki 
# getQuestionIndex fonk. ayni gorevde kullanilabiliyor.
# getQuestionIndex fonk. sayesinde bu kod bloğuna ihtiyaç duymuyoruz.
 """
quiz.loadquesstion()
#print(q1.check_answer('Java'))