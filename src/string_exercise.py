class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        return input_str[::-1]

    def is_english_vowel(self, character):
        if character.lower() in ('a', 'e', 'i', 'o', 'u'):
            return True
        else:
            return False

    def find_longest_word(self, sentence):
        longest = max(sentence.split(), key=len)
        return longest

    def get_word_lengths(self, text):
        sizeList = []
        
        for word in text.split(): 
            sizeList.append(len(word))
        return sizeList