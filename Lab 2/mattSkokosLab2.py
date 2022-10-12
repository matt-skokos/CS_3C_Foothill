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
        start = time.time()
        self.word_dict = self.load_file('latin.txt')
        stop = time.time()
        self.dict_load = stop - start

    def load_file(self, file):
        """Loads a text file in the format:( word, word \n )
        into a dictionary {keys = latin : values = english}.
        """
        word_dict = {}  # O(n)
        with open(file) as file_handle:  # O(1)
            for line in file_handle:  # O (3129n)
                try:  # O (n)
                    latin, english = line.split(",", maxsplit=1)  # O(3129n)
                    latin = latin.strip()  # O(3129n)
                    word_dict[latin] = english  # O(3129n)
                except ValueError:  # O(1)
                    continue
        return word_dict  # O(1)
    # final complexity:  O(1)

    def latin_to_english(self, trans_phrase):
        """ Will split() and translate a phrase of words into a list,
        then return this list as a new string with all words that were
        successfully translated.
        """
        word_list = trans_phrase.split()  # O(1)

        translation = []  # O(1)
        for word in word_list:  # O(n)
            if not self.word_dict.get(word):  # O(1)
                translation.append(word)  # O(n)
            if self.word_dict.get(word):  # O(1)
                translation.append(self.word_dict[word].rstrip())  # O(n)

        return " ".join(translation)
        # final func complexity: O(n)

    def user_menu(self):
        """ This will prompt the user for English word input"""
        while True:
            phrase = input("Please enter a latin phrase to translate: ")
            if phrase == 'exit':
                self.list_runtimes()
                break
            start = time.time()
            print(f"English translation: "
                  f"{self.latin_to_english(phrase)}")
            stop = time.time()
            total = stop - start
            Translator.__runtime_benchmarks.append(total + self.dict_load)

    def list_runtimes(self):
        """ Lists all entries in the movie list. """

        print("Here are your translation algorithm runtimes:".center(55))
        counter = 1
        for item in Translator.__runtime_benchmarks:
            print(f'{counter}  - {item:.11f}')
            counter += 1