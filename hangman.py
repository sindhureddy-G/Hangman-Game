import random
words=['cat','dog','sun','fruit','eggs']
word=random.choice(words)
guessed=["_"]*len(word)
attempts=6
print("Welcome to Hangman:")
print(" ".join(guessed))
while attempts>0 and "_" in guessed:
  x=("Guess a letter:")
  guess=input(x).lower()
  if guess in word:
     print("correct")
     for i in range(len(word)):
       if word[i]==guess:
        guessed[i]=guess
  else:
      attempts-=1
      print("wrong! Attempts left are:",attempts)
if "_" in guess:
    print("you lost! the word is:",word)
else:
    print("You won!,the word is:",word)
