list1 = [1, 0, 0, "w", 3, 0, 4, 5, 0, [5, 5, 5]]
list2 = []
while list1.__contains__(0):
    list1.remove(0)
    list2.append(0)
list1.extend(list2)
print(list1)
