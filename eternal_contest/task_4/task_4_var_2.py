def get_sum_increase(max_amount_number, numbers):
    stack = []
    for number in numbers:
        number_str = str(number)
        for i in range(len(number_str)):
            digit = number_str[-(i + 1)]
            if digit != 9:
                stack.append(10**i * (9 - int(digit)))
        stack.sort(reverse=True)
    return sum(stack[:max_amount_number])


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
