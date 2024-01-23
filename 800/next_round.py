# https://codeforces.com/problemset/problem/158/A

n, k = input().split(' ')
n = int(n)
k = int(k)

scores = input().split(' ')
advance = 0

if 1 <= k <= n and n <= 50:
    for score in scores:
        try:
            if int(score) > 0 and int(score) >= int(scores[k-1]):
                advance += 1
        except:
            pass

    print(advance)

