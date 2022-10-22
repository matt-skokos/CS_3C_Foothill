def palindrome(s):
    print(len(s) // 2)
    if len(s) % 2 == 0:
        mid = len(s)//2
        return palindrome(s[mid:]) == palindrome(s[:mid])


string = 'acaca'
string1 = 'baab'

print(palindrome(string))