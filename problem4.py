
import random

class Machine:
    def __init__(self, word_list):
        self.word_list = word_list

    def player(self, length):
        return Player(self.word_list, length)

class Player:
    def __init__(self, word_list, length):
        self.word_list = [word for word in word_list if len(word) == length]
        self.guesses = set()
        self.remaining = set('abcdefghijklmnopqrstuvwxyz')
        self.word = '_' * length
        self.failed = 0

    def guess(self, letter):
        if letter in self.guesses:
            raise ValueError('You already guessed that letter')

        self.guesses.add(letter)
        if letter in self.remaining:
            self.remaining.remove(letter)
            for i, char in enumerate(self.word_list[0]):
                if char == letter:
                    self.word = self.word[:i] + letter + self.word[i+1:]
            return self.word
        else:
            self.failed += 1
            return None

    def get_status(self):
        return f'Word: {self.word}, Remaining: {"".join(sorted(self.remaining))}, Failed: {self.failed}'

    def is_game_over(self):
        return self.failed >= 11 or '_' not in self.word

word_list = ['printable', 'hangman', 'python', 'computer', 'language', 'programming']

machine = Machine(word_list)
player = machine.player(9)

while not player.is_game_over():
    print(player.get_status())
    letter = input('Guess a letter: ')
    result = player.guess(letter)
    if result is None:
        print(f'{letter} is not in the word')
    else:
        print(result)

if '_' not in player.word:
    print(f'Congratulations, you won! The word was {player.word}')
else:
    print(f'Sorry, you lost. The word was {player.word_list[0]}')
