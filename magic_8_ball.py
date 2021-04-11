import random # import random module

def getAnswer(answerNumber): # getAnswer function defined
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


print(getAnswer(random.randint(1, 9))) # shortened version of below

# r = random.randint(1 , 9) # using random module to generate a number 1 <= r =< 9
# fortune = getAnswer(r) # getAnswer function called with r as argument, which stored in answerNumber parameter
# print(fortune) # print the statement associated
