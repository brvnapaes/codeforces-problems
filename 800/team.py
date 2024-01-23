# https://codeforces.com/problemset/problem/231/A

n = int(input())
lines = []
result = 0

for i in range(n):
    lines.append(input())

for line in lines:
    x, y, z = line.split(' ')
    x = int(x)
    y = int(y)
    z = int(z)
    if x + y + z >= 2:
        result += 1

print(result)