def removeAll(list, n):
    for i in range(list.count(n)):
        list.remove(n)
    
    return list


my_list = [1, 2, 3, 5, 1]

print(my_list)
print(removeAll(my_list, 1))


# [1, 2, 3, 5, 1]
# [2, 3, 5, 1]
# [2, 3, 5]
# 2