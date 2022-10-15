import time

""" 
Matt Skokos - Foothill College : CS3C
Lab Assignment #2 : Timing and Big O
Date: 10-11-2022
Description: The Translator class will model an dictionary lookup tool 
for phrases input by the user.  It can load a dictionary of the given 
form in a text file and output the results of the translation process. 
For this instance it will translate Latin phrases to English.
"""


class Translator:
    __runtime_benchmarks = []

    def __init__(self):
        self.word_dict = self.load_file('latin.txt')

    def load_file(self, file):
        """Loads a text file in the format:( word, word \n )
        into a dictionary {keys = latin : values = english}.
        """
        word_dict = {}
        with open(file) as file_handle:
            for line in file_handle:
                try:
                    latin, english = line.split(",", maxsplit=1)
                    latin = latin.strip()
                    word_dict[latin] = english
                except ValueError:
                    continue
        return word_dict

    def latin_to_english(self, trans_phrase):
        """ Will split() and translate a phrase of words into a list,
        then return this list as a new string with all words that were
        successfully translated.
        """
        word_list = trans_phrase.split()

        translation = []
        for word in word_list:
            if not self.word_dict.get(word):
                translation.append(word)
            if self.word_dict.get(word):
                translation.append(self.word_dict[word].rstrip())

        return " ".join(translation)

    def user_menu(self):
        """ This will prompt the user for English phrase input and
        handle collecting benchmark results.. """
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
        """ Lists all entries list of run-time benchmark results. """

        print("Here are your translation algorithm runtimes:".center(55))
        counter = 1
        for item in Translator.__runtime_benchmarks:
            print(f'{counter}  - {item:.13f}')
            counter += 1