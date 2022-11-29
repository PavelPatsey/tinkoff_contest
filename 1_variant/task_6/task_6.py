def get_answer(students):
    i = 0
    even_stack = []
    odd_stack = []
    while i < len(students):
        if (i + students[i]) % 2 == 0:
            if students[i] % 2 == 0:
                even_stack.append(i)
            else:
                odd_stack.append(i)
        i += 1

    if len(even_stack) == 1 and len(odd_stack) == 1:
        return even_stack[0] + 1, odd_stack[0] + 1
    else:
        return -1, -1


def read_input():
    students_len = int(input().strip())
    students = list(map(int, input().strip().split()))
    return students_len, students


def main():
    students_len, students = read_input()
    print(*get_answer(students))


if __name__ == "__main__":
    main()


"""
Ввод
4
2  1  4  6
Вывод
-1  -1

Ввод
2
1  2
Вывод
-1  -1

Ввод
2
2  1
Вывод
1 2

Ввод
8
1 2 6 4 5 3 7 8
Вывод
3 6

Ввод
8
1 2 6 4 5 3 7 8 10
Вывод
3 6
"""
