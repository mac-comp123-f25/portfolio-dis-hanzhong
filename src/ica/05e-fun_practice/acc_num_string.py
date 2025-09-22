def string_of_nums(num):

    return "".join(str(i) for i in range(1, num + 1))


print(string_of_nums(10))