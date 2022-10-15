from timeit import Timer

"""
How do you measure speed of functions in python?
How do lists/dicts perform ?

"""
# creating Timer object
t1 = Timer("print('action', end = ' ')", "print('setup')")

n = 5
secs = t1.timeit(number=n)

print(f'\n{n} times took {secs:.8f}')

print('\n', "-" * 20, "\n\n")

times = t1.repeat(10, 2)
for t in times:
    print(f"{t:.8f} Seconds", end=" // ")

print("\n", "*" * 100, "\n")


# testing out some list timing
def build_list(n):
    return list(range(n))


def access(list):
    list[0]
    list[n // 2]
    list[n - 1]


n = 100
t2 = Timer("access(l1)", "from __main__ import access, build_list,n; l1 = build_list(n)")
times = t2.repeat(25, 1)

secs = [x / 3 for x in times]

for t in secs:
    print(f"{t:.12f} secs")

print(f"best time {min(secs):.11f}")


def build_dict(n):
    return {i: str(i) for i in range(n)}

def inx(x, n): # do in front, middle, end and not found
    str(0) in x
    str(n//2) in x
    str(n-1) in x
    str('a') in x # not in x, valid but not in data

timeList = Timer('inx(x,n)',
                 'from __main__ import n, build_list, inx; x = build_list(n)') # setup

timeDict = Timer(
    'inx(x, n)',
    'from __main__ import n, build_dict, inx; x = build_dict(n)')

print('N', '\t', 'List', '\t', 'Dict')
for size in range(100, 10000+1, 5000):
    n = size
    list_secs = timeList.repeat(5, 5)
    dict_sect = timeDict.repeat(5, 5)
    print(n, '\t', min(list_secs), '\t', min(dict_sect))

# print(dir()) shows entire program namespace
