"""
Test driver to present a run environment for the Translator class
using a Latin - English dictionary.

Benchmark results of run-time performance:

Please enter a latin phrase to translate: subductisupercilicarptor betizare sunt
English translation: subductisupercilicarptor betizare sunt
Please enter a latin phrase to translate: in vinum veritas
English translation:  in  wine  truth
Please enter a latin phrase to translate: vulnero vulgivagus vindico villa redemptio redarguo recordor quotiens quotienscumque quisquis quinquennis quinam veni vidi vici
English translation:  wound  wandering  avenge  country  ransoming  disprove  remember  often  however  whoever  five  which  come  see  conquer
Please enter a latin phrase to translate: cogito ergo cogito repetitio
English translation:  think  therefore  think  repetition
Please enter a latin phrase to translate: fas est et ab hoste doceri
English translation:  divine  is  and ab hoste doceri
Please enter a latin phrase to translate: admoveo velociter lente pullus hospes terra
English translation:  move  quickly  slowly  young  guest  earth
Please enter a latin phrase to translate: abbas
English translation:  father
Please enter a latin phrase to translate: exit
     Here are your translation algorithm runtimes:
1  - 0.0087685585022
2  - 0.0080428123474
3  - 0.0099050998688
4  - 0.0090262889862
5  - 0.0080440044403
6  - 0.0078492164612
7  - 0.0031263828278


Big O notation of Algorithm:
load_file():
T(n) = 1(n) + 7 ---> Big-O = O(n)

latin_to_english():
T(n) = 1(n) + 6 ---> Big-O = O(n)

Algorithm Complexity --->    Big-0 = O(n)


Latin strings to check:

in vinum veritas
vulnero vulgivagus vindico villa redemptio redarguo recordor quotiens quotienscumque quisquis quinquennis quinam veni vidi vici
cogito ergo cogito repetitio
fas est et ab hoste doceri
subductisupercilicarptor betizare sunt
admoveo velociter lente pullus hospes terra
abbas
"""

from mattSkokosLab2 import Translator



def main():
    translate1 = Translator()
    translate1.user_menu()


if __name__ == "__main__":
    main()

