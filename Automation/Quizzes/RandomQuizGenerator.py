#! python3
# RandomQuizGenerator.py - Creates quizzes with questions
# in random order , along with the answer key. 

import random 
# the quiz data, keys are countries and values are their capitals
capitals = {'Afghanistan' : 'Kabul', 'Albania' : 'Tirana',
            'Algeria' : 'Algiers', 'Andorra' : 'Andorra la Vella',
            'Angola' : 'Luanda', 'Argentina' : 'Buenos Aires',
            'Australia' : 'Canberra', 'Austria' : 'Vienna',
            'Bahamas' : 'Nassau' , 'Bahrain' : 'Manama',
            'Belgium' : 'Brussels', 'Brazil' : 'Brasilia',
            'Canada' : 'Ottawa' , 'Chile' : 'Santiago',
            'China' : 'beijing' , 'Egypt' : 'Cairo',
            'England' : 'London', 'Germany' : 'Berlin',
            'Hungary' : 'Budapest', 'India' : 'New Delhi',
            'Iran' : 'Tehran', 'Ireland' : 'Dublin',
            'Italy' : 'Rome', 'Japan' : 'Tokyo',
            'Lebanon' : 'Beirut', 'Poland' : 'Warsaw',
            'Qatar' : 'Doha', 'Russia' : 'Moscow',
            'Senegal' : 'Dakar', 'Spain' : 'Madrid',
            'Sweden' : 'Stockholm', 'Syria' : 'Damascus'}


# Generate 5 quiz files
for quizNum in range(5):
    #Create the quiz and answer key files
    quizfile = open(f'capitalsquiz{quizNum + 1}.txt', 'w')
    # we add the 'w' to make the file ready to write
    answerKeyFile = open(f'capitalsquiz_answers{quizNum + 1}.txt','w')
    # now we write the header of the quiz file
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + f'Countries Capitals Quiz (Form{quizNum + 1})') 
    quizfile.write('\n\n')
    # shuffle the order of the countries 
    countries = list(capitals.keys())
    random.shuffle(countries)
    # loop throgh 32 countries, making
    # a question for each
    for questionNum in range(32):
        # we get the correct answer fro mthe shuffled
        # countries list to retrive from the 
        # the captials dictionnary
        correctAnswer = capitals[countries[questionNum]]
        # now we get all the capitals into a list
        wrongAnswers = list(capitals.values())
        # the we delete the correct answer from the lsit
        # to prevent duplciations
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # then we get three random answers from 
        # the wrong answers list
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        # write the question and the answer options to the
        # Quiz file
        quizfile.write(f'{questionNum + 1 }. What is the captila of {countries[questionNum]}?\n')
        for i in range(4):
            quizfile.write(f" {'ABCD'[i]}. {answerOptions[i]}\n")
        quizfile.write('\n')
        # write the answer key to a file
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizfile.close()
    answerKeyFile.close()
        

