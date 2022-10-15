import time

"""
Here's some gibberish to check if the gibberish flies.

"""

# simple addition function

def sum_of_n(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum += i
    stop = time.time()

    return the_sum, stop-start

print("times for n = ", 100000)
for times in range(5):
    print(f"Sum is {sum_of_n(100000)[0]}  required {sum_of_n(100000)[1]:.7f} seconds.")

"""
Big - Omega ( O ) 
    - approach: break the algorithm into the number of steps involved
         How many times does something move in / out of memory?
    - we would count the # of assignments
the_sum = 0               ----->  1 assignment to the_sum
for i in range(1, n+1):   ----->  n assignments to i
    the_sum += i          -----> n assignments to 'the_sum'
stop = time.time()

total for this algo = 1 + 2n assignments .......
total becomes Times(n) > T(n)  where n is known as the size of the problem
T(n) = 1 + 2n      as 'n' gets larger the first expression becomes insignificant
significant term = 2n    or just..... n


f(n)              Name
1                Constant
log(n)           Logarithmic
n                Linear
n log(n)         Log Linear
n^2              Quadratic
n^3              Cubic
2^n              Exponential
n!               Fuckin sad just really fuckin sad. Factorial
"""