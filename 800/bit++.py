# https://codeforces.com/problemset/problem/282/A

n = int(input())
statement = ''
result = 0

for _ in range(n):
    statement = input()
    if "++" in statement:
        result += 1
    elif "--" in statement:
        result -= 1

print(result)