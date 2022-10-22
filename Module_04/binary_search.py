#iterative
def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

demolist = [0, 1, 2, 8, 11, 12, 15, 31, 33,]
print(binary_search(demolist, 7))
print(binary_search(demolist, 31))


#recursive
def binary_search_recursive(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                print(midpoint, item)
                return binary_search_recursive(alist[:midpoint], item)
            else:
                print(midpoint, item)
                return binary_search_recursive(alist[midpoint + 1:], item)

demolist = [0, 1, 2, 8, 11, 12, 15, 31, 33,]
print(binary_search_recursive(demolist, 4))
print(binary_search_recursive(demolist, 31))