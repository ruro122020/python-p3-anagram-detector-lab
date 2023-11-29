# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        words = list()
        for word in word_list:
            letters = [letter for letter in word]
            if sorted(self.word) == sorted(letters):
                words.append(word)
        if len(words) > 0:
            return words
        else: 
            return words