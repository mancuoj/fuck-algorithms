n = int(input())

path = [0 for _ in range(n)]
used = [False for _ in range(n)]


def dfs(u):
    if u == n:
        for i in range(n):
            print(path[i] + 1, end=" ")
        print()
    else:
        for i in range(n):
            if not used[i]:
                path[u] = i
                used[i] = True
                dfs(u + 1)
                path[u] = 0
                used[i] = False


dfs(0)
