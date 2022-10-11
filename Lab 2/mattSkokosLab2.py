
import time

""" 
The Translator class will model an dictionary lookup tool for 
phrases input by the user.  It can load a dictionary of the given form
in a text file and output the results of the translation process. For 
this instance it will translate Latin phrases to English.
"""


class Translator:
    __runtime_benchmarks = []

    def __init__(self):
        pass

    def load_file(self, file):
        """Loads a text file in the format:( word, word \n )
        into a dictionary {keys = latin : values = english}.
        """
        word_dict = {}  # O(n)
        with open(file) as file_handle:  # O(1)
            for line in file_handle:  # O (n)
                try:  # O (n)
                    latin, english = line.split(",", maxsplit=1)  # O(n)
                    latin = latin.strip()  # O(n)
                    word_dict[latin] = english  # O(n)
                except ValueError:  # O(n)
                    continue
        return word_dict  # final func complexity : O(n)

    def latin_to_english(self, trans_phrase):
        """ Will split() and translate a phrase of words into a list,
        then return this list as a new string with all words that were
        successfully translated.
        """
        word_list = trans_phrase.split()  # O(n)

        translation = []  # O(n)
        for word in word_list:  # O(n)
            if word not in self.word_dict.keys():  # O(n)
                translation.append(word)  # O(1)
            if word in self.word_dict.keys():  # O(n)
                translation.append(self.word_dict[word].rstrip())  # O(1)

        return " ".join(translation)  # final func complexity: O(n)

    def user_menu(self):
        """ This will prompt the user for English word input"""
        while True:
            phrase = input("Please enter a latin phrase to translate: ")
            if phrase == 'exit':
                self.list_runtimes()
                break
            start = time.time()
            self.word_dict = self.load_file('latin.txt')
            print(f"English translation: "
                  f"{self.latin_to_english(phrase)}")
            stop = time.time()
            total = stop - start
            Translator.__runtime_benchmarks.append(total)

    def list_runtimes(self):
        """ Lists all entries in the movie list. """

        print("Here are your translation algorithm runtimes:".center(55))
        counter = 1
        for item in Translator.__runtime_benchmarks:
            print(f'{counter}  - {item:.13f}')
            counter += 1