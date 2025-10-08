def remove_all(value, lst):

    while value in lst:
        lst.remove(value)

numbers = [1, 2, 3, 2, 4, 2, 5]
remove_all(2, numbers)
print(numbers)

