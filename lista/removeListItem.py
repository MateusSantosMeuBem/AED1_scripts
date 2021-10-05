def removeAll(list, n):
    for item in range(len(list) - 1, -1, -1):
        if list[item] == n:
            del list[item]
    
    return list

my_list = [1, 5, 6, 1 , 3, 3, 4]

print(removeAll(my_list, 1))
