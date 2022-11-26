# id решения 2571153


def get_internet_costs(A, B, C, D):
    costs = A + (D - B) * C if D - B > 0 else A
    return costs


def read_input():
    return tuple(map(int, input().strip().split()))


def main():
    A, B, C, D = read_input()
    print(get_internet_costs(A, B, C, D))


if __name__ == "__main__":
    main()

"""
Ввод 
100  10  12  15
Вывод
160

Ввод 
100  10  12  1
Вывод
100
"""
