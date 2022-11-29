if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    all_problem = [None, None]
    for i, n in enumerate(numbers):
        if i % 2 == 0 and n % 2 == 0:
            if all_problem[0] is not None:
                print(-1, -1)
                break
            all_problem[0] = i + 1

        if i % 2 == 1 and n % 2 == 1:
            if all_problem[1] is not None:
                print(-1, -1)
                break
            all_problem[1] = i + 1
    else:
        if all_problem[0] is None and all_problem[1] is None:
            if len(numbers) >= 3:
                print(0, 2)
            else:
                print(-1, -1)
        else:
            print(*all_problem)


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
-1 -1
"""
