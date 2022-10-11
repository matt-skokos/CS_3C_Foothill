from mattSkokosLab2 import Translator


def timer(self, func):
    """ Runs the program functions in a simple benchmarking
    structure.  The return value will appear after the included
    functions return their output.
    """
    start = time.time()
    func()
    print("calculate time between here")

    stop = time.time()
    print(f"time: {(stop - start):2.7f}")
    return f'Run-time: {stop - start}'


def main():
    translate1 = Translator()
    # translate1.load_file('latin.txt')
    translate1.timer(translate1.load_file('latin.txt'))


if __name__ == "__main__":
    main()

"""
strange question but is strip better than or the same as replace here?
latin = latin.strip(',')
latin = latin.replace(',', '')

"""
