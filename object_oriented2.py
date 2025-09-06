class flashcasrd:
    
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + '(' + self.meaning + ')'
        

flash = []
print('Welcome to the flashcard app!')
while True:
    word = input('Enter the word you want to add to the flashcard: ')
    meaning = input('Enter the meaning of the word: ')

    flash.append(flashcasrd(word, meaning))
    option = int(input('Enter 0 to add more values \nEnter 1 to continue: '))
    if option:
        break
    
print("\nYour flashcards:")
for i in flash:
    print('>', i)