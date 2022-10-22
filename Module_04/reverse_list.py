"""
Think of a string as a recursive object....
ie. a string is composed of sub-strings
-note that the FIRST item is followed by the THE REST
so... if we reverse THE REST then put the first char on the end of that
we get a reversed string.

***Remember when working with sequences : EMPTY sequence, or ONE element
left***

"""

def reverse_string(s):
    if s == "":
        return s
    else:
        return reverse_string(s[1:]) + s[0]

string = 'abcdefg'
print(reverse_string(string))