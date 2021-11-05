'''
6
1 3 5 6 7 10
'''
import sys


def dfs(level, sum):
    if sum > total // 2: # 시간복잡도 줄이기
        return

    if level >= n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)  # 프로그램 종료

    else:
        dfs(level + 1, sum + a[level])
        dfs(level + 1, sum)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    dfs(0, 0)  # dfs(level(트리 레벨), sum)
    print("NO")
