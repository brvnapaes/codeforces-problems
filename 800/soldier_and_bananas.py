# https://codeforces.com/problemset/problem/546/A

k, n, w = input().split(' ')
total = 0
borrow = 0

for i in range(int(w)):
    total += int(k) * (i + 1)

if int(n) >= total:
    print('0')
else:
    print(total - int(n))
