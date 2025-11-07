# basics.py
def every_other(lst):
    result = []
    for i in range(0, len(lst), 2):
        result.append(lst[i])
    return result


def sum_positive(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

print(every_other([1, 3,5,7,9,11,12,13]))
print(sum_positive([-1,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))