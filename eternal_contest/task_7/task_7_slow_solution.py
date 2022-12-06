from collections import Counter


def is_circular(students):
    students_len = len(students)
    stack = set()
    next_student_number = 1
    current_student_number = None
    i = 0
    while i < students_len:
        current_student_number = next_student_number
        next_student_number = students[current_student_number - 1]
        stack.add(next_student_number)
        i += 1

    return len(stack) == students_len and next_student_number == 1


def get_redirected_students(students, from_whom_number, to_whom_number):
    redirected_students = students.copy()
    redirected_students[from_whom_number - 1] = to_whom_number
    return redirected_students


def get_answer(students):
    students_len = len(students)
    counter = Counter(students)

    if len(counter) == students_len - 1:
        keys = list(counter.keys())
        values = list(counter.values())

        if 2 in values:
            double_gifted_student_number = keys[values.index(2)]
        else:
            return (-1, -1)

        no_gifted_student_number = None
        i = 1
        number_is_found = False
        while not number_is_found and i <= students_len:
            if i not in keys:
                no_gifted_student_number = i
                number_is_found = True
            i += 1

        transactions = []
        i = 0
        while i <= students_len - 1:
            if students[i] == double_gifted_student_number:
                transactions.append((i + 1, no_gifted_student_number))
            i += 1

        for transaction in transactions:
            if is_circular(
                get_redirected_students(
                    students,
                    transaction[0],
                    transaction[1],
                ),
            ):
                return transaction

    return (-1, -1)


def read_input():
    students_len = int(input().strip())
    students = list(map(int, input().strip().split()))
    return students_len, students


def main():
    students_len, students = read_input()
    print(*get_answer(students))


if __name__ == "__main__":
    assert is_circular([1, 3, 1]) == False
    assert is_circular([2, 3, 1]) == True
    assert is_circular([2, 1, 4, 5, 3]) == False
    assert is_circular([2, 3, 2]) == False

    assert get_answer([1, 2, 3]) == (-1, -1)
    assert get_answer([1, 3, 1]) == (1, 2)
    assert get_answer([2, 1, 2, 3, 4]) == (1, 5)
    assert get_answer([2, 1, 4, 5, 3]) == (-1, -1)
    assert get_answer([2, 2]) == (2, 1)

    assert get_redirected_students([2, 2], 2, 1) == [2, 1]
    assert get_redirected_students([2, 1, 2, 3, 4], 1, 5) == [5, 1, 2, 3, 4]
    main()


"""
Ввод
3
1  2  3
Вывод
-1  -1  

Ввод
3
1  3  1
Вывод
1  2

Ввод
5
2 1 2 3 4
Вывод
1  5

Ввод
5
2 1 4 5 3
Вывод
-1 -1
"""
