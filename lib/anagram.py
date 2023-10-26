class Anagram:

    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])

    def match(self, possible_anagrams):
        anagram = []

        for word in possible_anagrams:
            if sorted(word) ==  self.word_letters:
                anagram.append(word)
        return(anagram)
    



# class Anagram:
#     def __init__(self, word):
#         self.word_letters = sorted([letter for letter in word])

#     def match(self, word_list):
#         match_word_list = []

#         for word in word_list:
#             if sorted([letter for letter in word]) == self.word_letters:
#                 match_word_list.append(word)

#         return match_word_list



listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
# So I think maybe creating a function that sorts through two words, and then passing
# into a loop that iterates through each word in the possible anagrams list.
    

