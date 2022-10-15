import time
#  "Checking off" solution Version 1
def anagramSolution1(s1, s2):
    alist = list(s2)

    pos1 = 0
    stillOk = True
    while pos1 < len(s2) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOk = False

        pos1 = pos1 + 1
    return stillOk

print(anagramSolution1('abcd', 'dcba'))

def anagramSolution1v2(s1, s2):
    if len(s1) != len(s2):
        return False
    n = len(s1)
    s2_list = list(s2)
    for c1 in s1:
        for i in range(len(s2_list)):
            if c1 == s2_list[i]:
                s2_list[i] = None
                n -= 1
                break
    return n == 0

def anagramSolution2(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()   # sort is a n log(n)

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches

def anagramSolution5(s1, s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOk = True
    while j<26 and stillOk:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOk = False
    return stillOk

print(anagramSolution5('apple', 'pleap'))

print(anagramSolution2('abcde', 'edcba'), 'final solution')
print(anagramSolution1v2('apple', 'leppa'))