# Wordle Game & Solver

So one day, a Medium Daily Digest showed up in my email. There were some Medium articles, and one article caught my attention, the one called [How to Wordle](https://jimstump.com/how-to-wordle-89612f758152). My first reaction was, "What is this? Is this a game?" and it got me interested. After I finished reading the article, I found out more about Wordle. I started trying that day's word (I managed to guess it right if I'm not mistaken even though my guesses were random because I haven't understood the game that well :sweat_smile:).

After a few days of playing the game, I thought it would be interesting to make a "helper" for this game. The first 2 videos that gave me the first hint of how I should make the solver are [Mahmood Hikmet's Video](https://www.youtube.com/watch?v=hJJaYvxQh8w) and [William Spaniel's Video](https://www.youtube.com/watch?v=gUiYsPgEslo).

## The Game
So, when I started to make my own version of the game, I didn't know that the original one would only give us common English words. So I looked for a complete English word list that includes words with ending (not only the root words). But later on, I figured out that it is necessary to have that word list. I downloaded the word list from [here](http://www.mieliestronk.com/wordlist.html) and saved it as **vocab.txt**. 

And also, I haven't implemented the proper handling for double letter guess. As [3Blue1Brown](https://www.youtube.com/watch?v=fRed0Xmc2Wg&list=PLj9KGGj9nSBSZa7y7ZXV29RPnxV_nuSkE) say in the video, there is some specific response that Wordle will give regarding double letter guess (I will use the example word from 3Blue1Brown, which is **SPEED**): 
1. If you guess with double letter word, but the answer only contains one letter of it, and both are in the wrong position, the left most of the double letter will only be yellow, and the other one will remain grey.
```
Guess : SPEED 
Answer : ABIDE
Clue : ⬛⬛🟨⬛🟨
```
2. If you guess with double letter word and the answer has the same double letter but in the wrong place, both will be yellow.
``` 
Guess : SPEED
Answer : ERASE
Clue : 🟨⬛🟨🟨⬛
```
3. If you guess with a double letter word, but the answer only contains one of the double letters, and one of the double letters is in the correct position, it will be green.
```
Guess : SPEED
Answer : STEAL
Clue : 🟩⬛🟩⬛⬛
```
4. If you guess with double letter word and the answer also has the same double letter but only one of them is in the right position, the one in the right position will be green and the other will be yellow.
```
Guess : SPEED
Answer : CREPE
Clue : ⬛🟨🟩🟨⬛
```

In my version of the game, I use another method to show the clue because it can only run on the terminal. Instead of using color, I use symbols such as :
* X for Grey
* ? for Yellow
* V for Green
