"""
Translator application:
1. It will load a file ( word, word \n ) into a dictionary
2. Convert line to couple with split() - latin word : key, english word: value
3. Menu to prompt user for english word input. ( use try / except to filter
 absent value )
4. goal: evaluate Python's dictionary form a PERFORMANCE standpoint
5. Also need to calculate time complexity of each function/line and the
whole program
6. finally translate 5 phrases in latin to english for sample run


Notes:
    - probably want a function to load, to parse and to function each line
    whichever runs faster
test phrase for word not in dictionary.
subductisupercilicarptor betizare
"""
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
        self.word_dict = self.load_file('latin.txt')

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
                break
            print(f"English translation: "
                  f"{self.latin_to_english(phrase)}")

    def timer(self, func):
        """ Runs the program functions in a simple benchmarking
        structure.  The return value will appear after the included
        functions return their output.
        """
        pass

    def list_runtimes(self):
        """ Lists all entries in the movie list. """
        counter = 1
        for item in Translator.__runtime_benchmarks:
            print(f'{counter}  - {item:.9f}')