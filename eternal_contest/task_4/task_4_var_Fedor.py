def f(k, a):
    "списки для каждого разряда"
    d = {i: [] for i in range(10)}
    """Заполним эти списки:
        для каждого числа
        разберем его на цифры
        каждую цифру сложим в соответствующий список"""
    for x in a:
        j = 0
        while x > 0:
            d[j].append(x % 10)
            j += 1
            x //= 10
    "начиная со старшего разряда"
    j = 9
    s = 0
    "пока еще есть разряды и хватает замен"
    while j >= 0 and k > 0:
        "отсортируем разряд"
        t = sorted(d[j])
        i = 0
        "пока хватает замен и есть цифры в разряде"
        while k > 0 and i < len(t):
            "заменим цифру на 9, если это не 9, добавим в сумму"
            if t[i] != 9:
                s += (9 - t[i]) * 10**j
                k -= 1
            i += 1
        j -= 1
    return s


def read_input():
    numbers_len, max_amount_number = tuple(map(int, input().strip().split()))
    numbers = list(map(int, input().strip().split()))
    return numbers_len, max_amount_number, numbers


def main():
    numbers_len, max_amount_number, numbers = read_input()
    print(f(max_amount_number, numbers))


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
