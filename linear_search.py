def linear_search(list, item):
    for i in list:
        while i != item:
            i += 1
            print(i)
        return print("The item has index: ", i)



list = list(range(1,100000001))
item = 100

print(linear_search(list, item))

