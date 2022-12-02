from collections import Counter
from itertools import permutations


def is_circular(students_len, students):
    stack = []
    next_student_number = 1
    i = 0
    while i < students_len:
        current_student_number = next_student_number
        next_student_number = students[current_student_number - 1]
        stack.append(next_student_number)
        i += 1
        
    counter = Counter(stack)
    return len(counter) == students_len


def redirect_gift(students, from_whom_number, to_whom_number):
    new_students = students.copy()
    new_students[from_whom_number - 1] = to_whom_number
    

    isCircular = is_circular(len(students), new_students)
    print(f"{new_students=} , {isCircular=}")

    return new_students


def get_answer(students_len, students):
    transactions = list(permutations(range(1, students_len + 1), 2))
    print(f"{transactions=}")
    zipped_students = list(zip(range(1, students_len + 1), students))
    print(f"{zipped_students=}")

    for transaction in transactions:
        print(f"{transaction=}")
        print(not transaction in zipped_students)
        if not transaction in zipped_students and is_circular(
            students_len,
            redirect_gift(
                students,
                transaction[0],
                transaction[1],
            ),
        ):
            return transaction[0], transaction[1]

    return (-1, -1)


def read_input():
    students_len = int(input().strip())
    students = list(map(int, input().strip().split()))
    return students_len, students


def main():
    # students_len, students = read_input()
    # print(*get_answer(students_len, students))

    # print(get_answer(2, [2, 2]))
    print(get_answer(3, [2, 3, 1]))
    pass


if __name__ == "__main__":
    # assert is_circular(3, [1, 3, 1]) == False
    # assert is_circular(3, [2, 3, 1]) == True
    # assert is_circular(5, [2, 1, 4, 5, 3]) == False
    assert is_circular(3, [2, 3, 2]) == False

    # assert get_answer(3, [1, 2, 3]) == (-1, -1)
    # assert get_answer(3, [1, 3, 1]) == (1, 2)
    # assert get_answer(5, [2, 1, 2, 3, 4]) == (1, 5)
    # assert get_answer(5, [2, 1, 4, 5, 3]) == (-1, -1)
    # assert get_answer(2, [2, 2]) == (2, 1)
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

Ввод
3
2  3  1
Вывод
-1  -1
"""
