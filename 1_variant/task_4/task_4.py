def get_modified_number(number):
    modified_number = ""
    digit_replaced = False
    for digit in str(number):
        if not digit_replaced and digit != "9":
            modified_number += "9"
            digit_replaced = True
        else:
            modified_number += digit
    return int(modified_number)


def get_difference_after_modification(number):
    return get_modified_number(number) - number


def get_sum_increase(max_amount_number, numbers):
    numbers.sort(key=get_difference_after_modification, reverse=True)
    stack = []
    difference = None
    i = 0
    while difference != 0 and i < max_amount_number:
        modified_number = get_modified_number(numbers[0])
        difference = modified_number - numbers[0]
        if difference != 0:
            numbers[0] = modified_number
            stack.append(difference)
            numbers.sort(key=get_difference_after_modification, reverse=True)
        i += 1
    return sum(stack)


def read_input():
    numbers_len, max_amount_number = tuple(map(int, input().strip().split()))
    numbers = list(map(int, input().strip().split()))
    return numbers_len, max_amount_number, numbers


def main():
    numbers_len, max_amount_number, numbers = read_input()
    print(get_sum_increase(max_amount_number, numbers))


if __name__ == "__main__":
    main()

"""
Ввод 
5 2
1 2 1 3 5
Вывод
16

Ввод 
3 1
99 5 85
Вывод
10

Ввод 
1 10
9999
Вывод
0

Ввод 
2 2
19 101
Вывод
890
"""
