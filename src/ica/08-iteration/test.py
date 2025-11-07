# whileloops.py

def add_user_nums():
    sum_of_nums = 0
    user_input = input("enter your number: ")
    num = float(user_input)
    while num != 0:
        sum_of_nums = sum_of_nums + num
        user_input = input("enter your number: ")
        num = float(user_input)
    return sum_of_nums


