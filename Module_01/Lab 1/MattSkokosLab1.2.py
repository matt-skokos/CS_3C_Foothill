"""
Matt Skokos - Foothill College : CS3C
Lab Assignment #1 : Objects and Classes
Date: 10-04-2022
Description: This program can be used to maintain a list of the user's
favorite films.  It has a menu to add/delete films and to display the
current films on the list.
"""
menuOptions = {
    'list': 'List all movies.',
    'add': 'Add a movie.',
    'del': 'Delete a movie.',
    'exit': 'Exit the program.'
}

class Movie:
    __moviesList = []
    DEFAULT_NAME = ""
    DEFAULT_YEAR = 2022

    def __init__(self, name=DEFAULT_NAME, year=DEFAULT_YEAR):
        if self.setName(name):
            self.name = name
        if self.setYear(year):
            self.year = year

    def list(self):
        """ Lists all entries in the movie list. """
        for item in Movie.__moviesList:
            print(f'item[0], item[1]')

    def setName(self, name):
        """ Setter mutator for Movie instance name value. """
        if self.strOK():
            self.name = name
            return True
        self.name = Movie.DEFAULT_NAME
        return False

    def setYear(self, year):
        """ Setter mutator for Movie instance name value. """
        if self.yearOK():
            self.year = year
            return True
        self.year = Movie.DEFAULT_YEAR
        return False

    def add(self, movieAdd):
        """ Adds an entry in the movie list. """
        Movie.__moviesList.append(movieAdd)

    def delete(self, listNum):
        """ Deletes an entry in the movie list by #. """
        Movie.__moviesList.pop(listNum)
        pass

    @staticmethod
    def displayMenu(self):
        """ Displays a command selection menu. """
        print("COMMAND MENU".center(55))
        for key in menuOptions:
            print(f'{key} : {menuOptions[key]}')

    def getStr(self):
        """ Returns a string representation of a movie entry. """
        return self.name

    def getYear(self):
        """ Returns the year of a movie entry. """
        return self.year

    @staticmethod
    def strOK(nameStr: str):
        """ Validates str parameters. """
        MAX_LENGTH = 50
        if isinstance(nameStr, str) and nameStr.isprintable() and \
                len(nameStr) <= MAX_LENGTH:
            return True

        pass

    @staticmethod
    def yearOK(year: int):
        """ Validates year parameters. """
        YEAR_LOW = 1000
        YEAR_HIGH = 2022
        if isinstance(year, int) and YEAR_LOW < year <= YEAR_HIGH:
            return True
