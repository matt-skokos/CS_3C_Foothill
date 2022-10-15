from mattSkokosLab1 import Movie

"""
Matt Skokos - Foothill College : CS3C
Lab Assignment #1 : Objects and Classes
File: mattSkokosLab1demo.py --- Driver File
Date: 10-04-2022
Description: This is the test driver program for the Movie class.  It
will demonstrate the class functions and data capabilities by providing
the user with a command menu and console output for their commands.
Sample run is included.
"""
menuOptions = {
    'list': 'List all movies.',
    'add': 'Add a movie.',
    'del': 'Delete a movie.',
    'exit': 'Exit the program.'
}


def main():
    """ Instantiate Movie class. """
    movie1 = Movie()

    """ Run command menu for user to test class methods. """
    while True:
        print("Movie List - COMMAND MENU".center(55))
        for key in menuOptions:
            print(f'{key} : {menuOptions[key]}')
        optionChoice = input("COMMAND: ")
        if optionChoice in menuOptions:
            print(f'You chose: {menuOptions[optionChoice]}')
            if optionChoice == 'exit':
                print("Thanks for using Movie List! Bye!")
                break
            if optionChoice == 'add':
                name = input('Name of movie: ')
                try:
                    year = int(input('Year of movie: '))
                except ValueError:
                    print("Please enter an integer for the year.")
                    continue
                movie1.add(name, year)
            if optionChoice == 'del':
                numChoice = int(input('Enter the number movie to '
                                      'delete: '))
                movie1.delete(numChoice)
            if optionChoice == 'list':
                movie1.list()
        else:
            print("Enter a valid command from the menu please.")
            continue


if __name__ == "__main__":
    main()


"""      --- SAMPLE RUN ---
      
               Movie List - COMMAND MENU               
list : List all movies.
add : Add a movie.
del : Delete a movie.
exit : Exit the program.
COMMAND: add
You chose: Add a movie.
Name of movie: The Terminator
Year of movie: 1984
               Movie List - COMMAND MENU               
list : List all movies.
add : Add a movie.
del : Delete a movie.
exit : Exit the program.
COMMAND: add
You chose: Add a movie.
Name of movie: Monty Python's Life of Brian
Year of movie: 1979
               Movie List - COMMAND MENU               
list : List all movies.
add : Add a movie.
del : Delete a movie.
exit : Exit the program.
COMMAND: add
You chose: Add a movie.
Name of movie: Batman & Robin
Year of movie: 1997
               Movie List - COMMAND MENU               
list : List all movies.
add : Add a movie.
del : Delete a movie.
exit : Exit the program.
COMMAND: add
You chose: Add a movie.
Name of movie: Citizen Kane
Year of movie: 1941
               Movie List - COMMAND MENU               
list : List all movies.
add : Add a movie.
del : Delete a movie.
exit : Exit the program.
COMMAND: list
You chose: List all movies.
1.  The Terminator  (1984)
2.  Monty Python's Life of Brian  (1979)
3.  Batman & Robin  (1997)
4.  Citizen Kane  (1941)
               Movie List - COMMAND MENU               
list : List all movies.
add : Add a movie.
del : Delete a movie.
exit : Exit the program.
COMMAND: del
You chose: Delete a movie.
Enter the number movie to delete: 3
You've deleted Batman & Robin.
               Movie List - COMMAND MENU               
list : List all movies.
add : Add a movie.
del : Delete a movie.
exit : Exit the program.
COMMAND: list
You chose: List all movies.
1.  The Terminator  (1984)
2.  Monty Python's Life of Brian  (1979)
3.  Citizen Kane  (1941)
               Movie List - COMMAND MENU               
list : List all movies.
add : Add a movie.
del : Delete a movie.
exit : Exit the program.
COMMAND: exit
You chose: Exit the program.
Thanks for using Movie List! Bye!

Process finished with exit code 0

"""