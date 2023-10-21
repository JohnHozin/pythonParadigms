sortList = [1, 6, 8, 23, 15, 34, 2, 9, 11, 4, 0, -6]


# Императивный
def sort_list_imperative(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


print(sort_list_imperative(sortList))


# Декларативный
def sort_list_declarative(numbers):
    return sorted(numbers)


print(sort_list_declarative(sortList))
