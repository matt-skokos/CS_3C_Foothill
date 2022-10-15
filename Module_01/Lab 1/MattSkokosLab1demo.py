from MattSkokosLab1 import Movie

"""This test driver will present a menu driven application to 
demonstrate the Movie class.
"""
# I've had to repeat this code to make my menu work
menuOptions = {
    'list': 'List all movies.',
    'add': 'Add a movie.',
    'del': 'Delete a movie.',
    'exit': 'Exit the program.'
}

def main():
    movie1 = Movie("", 0)
    while True:
        Movie.displayMenu(movie1)
        try:
            optionChoice = input("COMMAND: ")
        except ValueError:
            print("Enter a valid command from the menu please.")
            continue
        if optionChoice in menuOptions:
            print(f'You chose: {menuOptions[optionChoice]}')
            if optionChoice == 'exit':
                print("Thanks for using Movie List! Bye!")
                break
            if optionChoice == 'add':
                name = input('Name of movie: ')
                year = input('Year of movie: ')
                movie1.add((name, year))
            if optionChoice == 'del':
                numChoice = int(input('Enter the number movie to '
                                      'delete: '))
                movie1.delete(numChoice)
            if optionChoice == 'list':
                movie1.list()


if __name__ == "__main__":
    main()
