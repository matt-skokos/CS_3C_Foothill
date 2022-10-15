"""
Matt Skokos - Foothill College : CS3C
Lab Assignment #1 : Objects and Classes
Date: 10-04-2022
Description: This program can be used to maintain a list of the user's
favorite films.  It has a menu to add/delete films and to display the
current films on the list.
"""

menu_options = {
    'list': 'List all movies',
    'add': 'Add a movie',
    'del': 'Delete a movie',
    'exit': 'Exit program',
}


class Movie:
    __movieList = []

    def __init__(self, name="", year=2022):
        self.name = name
        self.year = year


    def list(self):
        for item in Movie.__movieList:
            print(f'{item[0]} : {item[1]}')

    def add(self, name: str, year: int):
        # Movie.__movieList.append((name, year))
        if self.strOK(name) and self.yearOK(year):
            Movie.__movieList.append(self.name, self.year)
            return True

    def delete(self, num: int):
        if num in Movie.__movieList:
            Movie.__movieList.pop(num)
            return True
        return False

    def displayMenu(self):
        """Displays the menu of options"""
        while True:
            print("COMMAND MENU".center(55))
            for key in menu_options:
                print(f"{key} : {menu_options[key]}")
            try:
                option_choice = input("Command: ")
            except ValueError:
                print("Enter a valid choice from the menu please.")
                continue
            if option_choice in menu_options:
                print(f"You chose: {menu_options[option_choice]}")
                if option_choice == "exit":
                    break
                if option_choice == 'add':
                    name = input("Name of movie: ")
                    year = input("Year of movie: ")
                    self.add(name, year)
                if option_choice == 'del':
                    num_choice = int(input("Enter a number to delete: "))
                    self.delete(num_choice)
                if option_choice == 'list':
                    self.list()

    def getStr(self):
        """ Returns a string representation of a movie"""
        return f"{self.name} : {self.year}"

    @staticmethod
    def strOK(name_str: str):
        """ Helper method validates string/name parameters. """
        MAX_LENGTH = 50
        if isinstance(name_str, str) and name_str.isprintable() and \
                len(name_str) <= MAX_LENGTH:
            return True

    @staticmethod
    def yearOK(year: int):
        """ Helper method to validate year value."""
        LOWEST_YEAR = 1000
        HIGHEST_YEAR = 2022
        if isinstance(year, int) and LOWEST_YEAR < year <= HIGHEST_YEAR:
            return True

    def setYear(self, year: int):
        """ Setter method for the year instance member. """
        if self.yearOK(year):
            self.year = year

    def setName(self, name: str):
        """ Setter method for the name instance member. """
        if self.strOK(name):
            self.name = name


def main():
    movie = Movie()
    movie.displayMenu()


if __name__ == "__main__":
    main()
