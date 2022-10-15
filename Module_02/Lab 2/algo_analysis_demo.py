"""
What should we measure?
    - clarity/simplicity?  - is it less error-prone?
    - space efficiency?
    - time efficiency?

Runtime Complexity/Analysis
    - So far ...how fast can it go? Empirical clock time
    - These things are sensitive to platform/concurrent tasks/implementation
    - measured runtime doesn't always help us see long-term/big picture


"""
numbers = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1]
# Order of n   O(n)
sum = 0
for num in numbers:
    sum += num

# Order of n * n   O(n^2)
sum = 0
for num1 in numbers:
    for num2 in numbers:  # important how many times the innermost loop
        # will run
        sum += 1

"""Informal description of Big-O: growth functions are categorized according 
to their dominant (fastest growing) term. Constants and lower-order terms 
are discarded.  Ex. 10n --> O(n), 
                5n^2 + 2n + 3 --> O(n^2), 
                nlogn + n --> O(nlogn)
Why drop constants? only concerned about fastest growing term
Also:
1. Big Omega - tighter lower bound, loosely analogous to >=
2. Big Theta - everything that is theta is also O(f(n)) but not vice-versa
big Theta is more informative than big-O notation (between two functions)
"""
vals = [1, 3, 44, 0]


def sort(vals):  # input size = len(vals)
    vals.sort()


def factorial(n):  # input size of n
    if (n == 1 or n == 0):
        return 1
    return n * factorial(n - 1)


print(factorial(14))
print("x")


def gcd(m, n):  # input size = (m, n)
    return m // n


"""
Calculating T(n)                       
def factorial(n):                          times
    prod = 1                               1
    for k in range(2, n+1):                n-1
        prod *= k                          n-1
    return prod                            1
    
So.... T(n) = 2(n-1) + 2 = 2n    ... ignore lines of code runtime is LINEAR
"""


def insertion_sort(lst):                                 # times
    for i in range(1, len(lst)):                         # n-1
        for j in range(i, 0, -1):                        # 1, 2 (n -1)
            if lst[j] < lst[j - 1]:                      # 1, 2, (n-1)
                lst[j], lst[j - 1] = lst[j - 1], lst[j]  # 1, 2 (n-1)
            else:                                        # 0
                break                                    # 0

#  you can have worst case, best case and more common case.
# worst case is the DEFAULT

def foo(n):
    for _ in range(n):
        for _ in range(n):
            for _ in range(n):
                pass

#  ^^^       n^3          ^^^^^^

#  binary search = 0(log n)

# factorial linear search  = O(n)

# insertion sort = O(n^2)

