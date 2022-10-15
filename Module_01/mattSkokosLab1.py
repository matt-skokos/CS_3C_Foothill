"""
Matt Skokos - Foothill College : CS3C
Lab Assignment #1 : Objects and Classes
File: mattSkokosLab1.py --- Class File
Date: 10-04-2022
Description: The Movie class is designed to maintain a list of the
user's favorite films.  It has a command menu to add/delete films and
to display the current films on the list.
"""


class Movie:
    __moviesList = []
    DEFAULT_NAME = ""
    DEFAULT_YEAR = 2022

    def __init__(self, name=DEFAULT_NAME, year=DEFAULT_YEAR):
        if self.setName(name) and self.setYear(year):
            self.name = name
            self.year = year

    def list(self):
        """ Lists all entries in the movie list. """
        counter = 1

        for movie in Movie.__moviesList:
            print(f'{counter}.  {movie.getStr()}')
            counter += 1

    def setName(self, name):
        """ Setter / mutator for Movie instance name value. """
        if self.strOK(name):
            self.name = name
            return True
        self.name = Movie.DEFAULT_NAME
        return False

    def setYear(self, year):
        """ Setter / mutator for Movie instance year value. """
        if self.yearOK(year):
            self.year = year
            return True
        self.year = Movie.DEFAULT_YEAR
        return False

    def add(self, name, year):
        """ Adds an entry in the movie list. """
        if self.strOK(name) and self.yearOK(year):
            Movie.__moviesList.append(Movie(name, year))

    def delete(self, listNum):
        """ Deletes an entry in the movie list by #. """
        try:
            movie_object = Movie.__moviesList.pop(listNum - 1)
            print(f"You've deleted {movie_object.getName()}.")

        except IndexError:
            print("You've entered a number that's not on the list.")

    def getName(self):
        """ Returns a string representation of the movie name. """
        return f'{self.name}'

    def getYear(self):
        """ Returns a string representation of the movie year. """
        return self.year

    def getStr(self):
        """ Returns a string representation of a movie entry. """
        return f'{self.getName()}  ({self.getYear()})'

    @staticmethod
    def strOK(nameStr: str):
        """ Validates str parameters. """
        MAX_LENGTH = 50
        if isinstance(nameStr, str) and nameStr.isprintable() and \
                len(nameStr) <= MAX_LENGTH:
            return True

    @staticmethod
    def yearOK(year: int):
        """ Validates year parameters. """
        YEAR_LOW = 1000
        YEAR_HIGH = 2022
        if isinstance(year, int) and YEAR_LOW < year <= YEAR_HIGH:
            return True
