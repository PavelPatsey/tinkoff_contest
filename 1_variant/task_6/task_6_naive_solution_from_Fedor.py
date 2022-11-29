def f(a):
    invalid_even_count = 0
    invalid_odd_count = 0
    for i, x in enumerate(a):
        if (i + 1) % 2 == 0 and x % 2 != 0:
            invalid_even = i + 1
            invalid_even_count += 1
        elif (i + 1) % 2 != 0 and x % 2 == 0:
            invalid_odd = i + 1
            invalid_odd_count += 1
    if invalid_odd_count == 1 and invalid_even_count == 1:
        if invalid_even > invalid_odd:
            return invalid_odd, invalid_even
        return invalid_even, invalid_odd
    return -1, -1


def read_input():
    students_len = int(input().strip())
    students = list(map(int, input().strip().split()))
    return students_len, students


def main():
    students_len, students = read_input()
    print(*f(students))


def naive(a):
    for i, j in combinations(range(len(a)), 2):
        if valid(swap(a, i, j)):
            return i + 1, j + 1
    return -1, -1


def valid(a):
    return all(x % 2 != 0 for x in a[::2]) and all(x % 2 == 0 for x in a[1::2])


def swap(a, i, j):
    b = a.copy()
    b[i], b[j] = b[j], b[i]
    return b


from itertools import combinations

assert f([2, 1, 4, 6]) == (-1, -1)
assert f([1, 2]) == (-1, -1)
assert f([2, 1]) == (1, 2)
assert f([1, 2, 6, 4, 5, 3, 7, 8]) == (3, 6)
assert f([1, 2, 6, 4, 5, 3, 7, 8, 10]) == (-1, -1)
assert naive([2, 1, 4, 6]) == (-1, -1)
assert naive([1, 2]) == (-1, -1)
assert naive([2, 1]) == (1, 2)
assert naive([1, 2, 6, 4, 5, 3, 7, 8]) == (3, 6)
assert naive([1, 2, 6, 4, 5, 3, 7, 8, 10]) == (-1, -1)

from random import sample

for _ in range(1000):
    a = sample(range(1, 1001), 10)
    if f(a) != naive(a):
        print(a, f(a), naive(a))

if __name__ == "__main__":
    main()
