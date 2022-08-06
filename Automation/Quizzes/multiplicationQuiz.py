import pyinputplus as pyip
import random, time

numberOfQuestions = 10
correctAnswers = 0 
for questionNumber in range(numberOfQuestions):
    #Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        # Right answers are handled by allowregexes
        # wrong answers are handled by blockregexes
        # .* match any character or more
        # ^%s$ macthes the result num1 x num2
        pyip.inputStr(prompt,allowRegexes=['^%s$' % (num1 * num2)],
                             blockRegexes=[('.*','Incorrect!')],
                             timeout=8, limit =3)  
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!') 
    else:
        #this block runs of no expections were triggered
        print('Correct!')
        correctAnswers += 1
    time.sleep(10) # pause to let the user see the result
print('score : %s / %s' % (correctAnswers,numberOfQuestions))