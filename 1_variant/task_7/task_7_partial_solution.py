from collections import Counter


def is_circular(students_len, students):
    stack = []
    next_student_index = 0
    stack.append(next_student_index)
    for _ in range(students_len):
        current_student_index = next_student_index
        next_student_index = students[current_student_index] - 1
        stack.append(next_student_index)

    counter = Counter(stack)
    return len(counter) == students_len


def redirect_gift(students, from_whom_number, to_whom_number):
    new_students = students.copy()
    new_students[from_whom_number - 1] = to_whom_number
    return new_students


def get_answer(students_len, students):
    counter = Counter(students)

    if len(counter) == students_len - 1:
        keys = list(counter.keys())
        values = list(counter.values())

        # print(f"{keys=}")
        # print(f"{values=}")
        double_gifted_student_number = keys[values.index(2)]

        no_gifted_student_number = None
        i = 1
        while i <= students_len:
            # print(i, keys)
            if i not in keys:
                no_gifted_student_number = i
            i += 1

        # print(f"{double_gifted_student_number=}")
        # print(f"{no_gifted_student_number=}")

        from_whom_numbers = []
        i = 0
        while i <= students_len - 1 and len(from_whom_numbers) <= 2:
            # print(f"{i=}, {students[i]=}")
            if students[i] == double_gifted_student_number:
                from_whom_numbers.append(i + 1)
            i += 1

        # print(from_whom_numbers)

        for number in from_whom_numbers:
            if is_circular(
                students_len,
                redirect_gift(
                    students,
                    number,
                    no_gifted_student_number,
                ),
            ):
                return number, no_gifted_student_number

    return (-1, -1)


def read_input():
    students_len = int(input().strip())
    students = list(map(int, input().strip().split()))
    return students_len, students


def main():
    students_len, students = read_input()
    print(*get_answer(students_len, students))


if __name__ == "__main__":
    # assert is_circular(3, [1, 3, 1]) == False
    # assert is_circular(3, [2, 3, 1]) == True
    # assert is_circular(5, [2, 1, 4, 5, 3]) == False

    # assert get_answer(3, [1, 2, 3]) == (-1, -1)
    # assert get_answer(3, [1, 3, 1]) == (1, 2)
    # assert get_answer(5, [2, 1, 2, 3, 4]) == (1, 5)
    # assert get_answer(5, [2,1,4,5,3]) == (-1, -1)
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
