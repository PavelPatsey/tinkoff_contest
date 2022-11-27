def get_modified_number_and_difference(number):
    modified_number = ""
    digit_replaced = False
    for digit in str(number):
        if not digit_replaced and digit != "9":
            modified_number += "9"
            digit_replaced = True
        else:
            modified_number += digit
    modified_number = int(modified_number)
    return modified_number, modified_number - number


def difference_after_all_replacements(x):
    return int("9" * len(str(x))) - x


def get_sum_increase(max_operations_number, numbers):
    numbers.sort(key=difference_after_all_replacements, reverse=True)
    stack = []
    difference = None
    i = 0
    while difference != 0 and i < max_operations_number:
        modified_number, difference = get_modified_number_and_difference(numbers[0])
        if difference != 0:
            numbers[0] = modified_number
        numbers.sort(key=difference_after_all_replacements, reverse=True)
        stack.append(difference)
        i += 1
    return sum(stack)


def read_input():
    numbers_amount, max_operations_number = tuple(map(int, input().strip().split()))
    numbers = list(map(int, input().strip().split()))
    return numbers_amount, max_operations_number, numbers


def main():
    numbers_amount, max_operations_number, numbers = read_input()
    print(get_sum_increase(max_operations_number, numbers))
    # print(get_modified_number_and_difference(99))


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

Ввод 
4 4
99 91 19 101
Вывод
978
"""
