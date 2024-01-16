m, n = input().split(' ')

m = int(m)
n = int(n)

result = 0

if n >= m >= 1 and n <= 16:
    if (m*n) % 2 == 0:
       result = m*n / 2
    else:
       result = (m*n - 1) / 2

print(int(result))

