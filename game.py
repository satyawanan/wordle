import random

def prepare_words():
    f = open("vocab.txt", "r")
    words = f.read()
    words = words.split('\n')

    five_words = []
    for word in words:
        if(len(word)==5):
            five_words.append(word)
    return five_words

def is_valid(guess):
    is_in_words = guess in WORDS
    is_len_five = len(guess) == 5

    return_message = None
    if(not is_len_five):
        return_message = "Please enter a 5 letter word"
    elif(not is_in_words):
        return_message = "Word not in dictionary"


    return is_in_words and is_len_five, return_message

def generate_solution():
    return WORDS[random.randint(0,len(WORDS)-1)]

def give_feedback(guess, solution):
    feedback = []
    for i in range(5):
        if(guess[i] in solution):
            if(guess[i] == solution[i]):
                feedback.append('V')
            else:
                feedback.append('?')
        else:
            feedback.append('X')
    return feedback

def is_done(feedback):
    count = feedback.count('V')
    if(count==5):
        return True
    else:
        return False

WORDS = prepare_words()

solution = generate_solution()

chance = 6
while(chance>0):
    guess = input('Your Guess : ')
    valid = is_valid(guess)
    if(valid[0]):
        feedback = give_feedback(guess, solution)
        print(feedback)
        if(is_done(feedback)):
            print('CONGRATULATION!!!')
            break
        chance-=1
    else:
        if(valid[1]):
            print(valid[1])