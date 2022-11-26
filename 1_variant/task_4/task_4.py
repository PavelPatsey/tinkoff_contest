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


def get_sum_increase(max_operations_number, numbers):
    numbers.sort(key=sum_after_replacement, reverse=True)
    print(f"{numbers=}")
    stack = []
    difference = None
    while difference != 0:
        get_modified_number, difference = get_modified_number_and_difference(numbers[0])
        numbers[0] = get_modified_number
        numbers.sort(key=sum_after_replacement, reverse=True)
        print(f"{get_modified_number=} {difference=}")
        print(f"{numbers=}")
        stack.append(difference)
    return sum(stack)


def sum_after_replacement(x):
    return int("9" * len(str(x))) - x


def read_input():
    numbers_amount, max_operations_number = tuple(map(int, input().strip().split()))
    numbers = list(map(int, input().strip().split()))
    return numbers_amount, max_operations_number, numbers


def main():
    numbers_amount, max_operations_number, numbers = read_input()
    print(get_sum_increase(max_operations_number, numbers))

    # print(numbers.sort(cmp=numeric_compare, reverse = True))
    # print(numbers.sort(cmp=numeric_compare))
    # print(sorted(numbers, key=sum_after_replacement, reverse=True))

    # a = 87
    # print(f"{a=}", get_modified_number_and_difference(a))
    # a = 99
    # print(f"{a=}", get_modified_number_and_difference(a))
    # a = 81862
    # print(f"{a=}", get_modified_number_and_difference(a))


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
1 10
99 91 19 101
Вывод
0
"""
