import sys

input = sys.stdin.readline


def backtracking():
    if len(array) == m:
        print(" ".join(map(str, array)))
        print()
        return

    for i in range(1, n + 1):
        if i not in array:
            print("append:", end=" ")
            array.append(i)
            # 1
            # 2
            # 3
            print(array)
            backtracking()
            print("pop: ", end=" ")
            array.pop()
            print(array)


# n, m = map(int, input().split())
n, m = 3, 3
array = []

backtracking()
