def binary_search(list, item):  #L and H edges of the list to search
    low = 0
    high = len(list)-1

    while low <= high:        # Check those parts till there is one element
        mid = int((low+high)/2)     #
        guess = list[mid]
        print(guess)
        if guess == item:     # the item is found!
            return mid
        if guess > item:      # too much
            high = mid-1
        else:                 # too low
            low = mid+1
    return None               # the item doesnt exist

list = list(range(1,100000001))
item = 50
print("The item has index: ", binary_search(list, item))

""" O(n) linear time - 10000000
    O(Log n) logarithmic time - 100000000 list, log(100000000, 2) = 26.57s
    O large counts the number of operations an algorithm will take in
    the worst case scenario"""


