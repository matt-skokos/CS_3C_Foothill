from mattSkokosLab2 import Translator


def user_menu(self):
    """ This will prompt the user for English word input"""
    while True:
        phrase = input("Please enter a latin phrase to translate: ")
        if phrase == 'exit':
            break
        print(f"English translation: "
              f"{.latin_to_english(phrase)}")
def main():
    translate1 = Translator()
    translate1.user_menu()


if __name__ == "__main__":
    main()

"""
strange question but is strip better than or the same as replace here?
latin = latin.strip(',')
latin = latin.replace(',', '')

"""
