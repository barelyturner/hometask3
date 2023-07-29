list1 = [1, "w", 3, 4, 5, [5, 5, 5]]
if list1 == []:
    print(list1)
else:
    list1.insert(0, list1.pop(-1))
    print(list1)
