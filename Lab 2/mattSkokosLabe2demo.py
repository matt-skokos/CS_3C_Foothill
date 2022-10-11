from mattSkokosLab2 import Translator

def main():
    translate1 = Translator()
    translate1.load_file('latin.txt')
    translate1.timer()


if __name__ == "__main__":
    main()

"""
strange question but is strip better than or the same as replace here?
latin = latin.strip(',')
latin = latin.replace(',', '')


"""