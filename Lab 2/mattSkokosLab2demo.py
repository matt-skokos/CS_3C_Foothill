"""
Benchmark results of run-time performance:


Big O notation of Algorithm:
load_file():
T(n) = 5(n) + 4 ---> Big-O = O(n)

latin_to_english():
T(n) = 3(n) + 4 ---> Big-O = O(n)




"""

from mattSkokosLab2 import Translator



def main():
    translate1 = Translator()
    translate1.user_menu()


if __name__ == "__main__":
    main()

"""

strings to check:
in vinum veritas
cogito ergo cogito repetitio cogito
fas est et ab hoste doceri   - won't work fully
subductisupercilicarptor betizare  - won't work at all
admoveo velociter lente pullus hospes terra
abbas


It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way—in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only. 

"""
