import string

def prepare_words():
    f = open("vocab.txt", "r")
    words = f.read()
    words = words.split('\n')

    five_words = []
    for word in words:
        if(len(word)==5):
            five_words.append(word)
    return five_words

def prepare_scores():
    return {i:[0,0,0,0,0] for i in ALPHABET}

def process_guess(guess, feedback):
    new_wrong_letters = []
    for i in range(5):
        if(feedback[i] == 'X'):
            if(guess[i] not in WRONG_LETTERS):
                new_wrong_letters.append(guess[i])
            WRONG_LETTERS.append(guess[i])
        elif(feedback[i] == '?'):
            if(guess[i] not in CORRECT_LETTERS):
                CORRECT_LETTERS.append(guess[i])
        else:
            if(guess[i] not in CORRECT_LETTERS):
                CORRECT_LETTERS.append(guess[i])
            CORRECT_POSITION[i] = guess[i]
    return new_wrong_letters

def remove_X():
    res = [w for w in WORDS if all(chr not in w for chr in WRONG_LETTERS)]
    return res

def remove_question(guess, feedback):
    res = []
    if(len(CORRECT_LETTERS) > 0):
        for w in WORDS:
            is_append = True
            for c in CORRECT_LETTERS:
                if(c not in w):
                    is_append = False
            for i in range(5):
                if(feedback[i] == '?'):
                    if(guess[i] == w[i]):
                        is_append = False
            if(is_append):
                res.append(w)
        return res 
    else:
        return WORDS

def remove_V():
    res = []
    for w in WORDS:
        is_append = True
        for i in range(5):
            if(CORRECT_POSITION[i] != '0'):
                if(CORRECT_POSITION[i] != w[i]):
                    is_append = False
        if(is_append):
            res.append(w)
    return res

def update_alphabet(new_wrong_letters):
    a = ALPHABET
    for i in a:
        if(i in new_wrong_letters):
            a = a.replace(i,'')
    return a

def update_scores():
    for i in range(5):
        pos_letters = [w[i] for w in WORDS]
        for j in ALPHABET:
            SCORES[j][i] += pos_letters.count(j)

def generate_rec():
    word_scores = {i:0 for i in WORDS}
    for w in WORDS:
        score = 0
        for i in range(5):
            score += SCORES[w[i]][i]
        word_scores[w] = score

    for key in word_scores:
        if any(key.count(i) > 1 for i in key):
            word_scores[key] -= 100
        
    rec_words = sorted(word_scores, key=word_scores.get, reverse=True)[:10]
    
    scr = []
    for rw in rec_words:
        scr.append(word_scores[rw])
    return rec_words
    # print(scr)

def show_rec(rec):
    print('Word Recommendation : ')
    for i in range(0,len(rec)):
        print(f'{i+1}. {rec[i]}')
    print('\n')

WORDS = prepare_words()
SCORES = {}
WRONG_LETTERS = []
CORRECT_LETTERS = []
CORRECT_POSITION = ['0' for i in range(5)]
ALPHABET = string.ascii_lowercase

new_wrong_letters = []
attempt = 6

guide = """
Guide : 
1. Type your answer
2. Feedback meaning :
- X : Letter not exist
- ? : Letter exist but in the wrong position
- V : Letter in the right position
"""
print(guide)

SCORES = prepare_scores()
update_scores()
rec = generate_rec()
show_rec(rec)

while(attempt > 0):
    guess = (input('Your Guess : ')).lower()
    feedback = input('Feedback : ')

    if(len(guess) != 5 or len(feedback) != 5):
        print('Guess and Feedback have to be 5 characters \n')
        continue

    if not all(i in ['V', '?','X'] for i in feedback):
        print('Feedback has to be V, ?, or X \n')
        continue

    if all(feedback[i] == 'V' for i in range(5)):
        print('CONGRATULATION!!!')
        break
    print(attempt)
    new_wrong_letters = process_guess(guess, feedback)
    WORDS = remove_X()
    WORDS = remove_question(guess, feedback)
    WORDS = remove_V()

    ALPHABET = update_alphabet(new_wrong_letters)
    SCORES = prepare_scores()
    update_scores()
    rec = generate_rec()
    show_rec(rec)

    attempt-=1