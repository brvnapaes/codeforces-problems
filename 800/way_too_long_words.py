# https://codeforces.com/problemset/problem/71/A

n = int(input())
i = 0
words = []

if 1 <= n <= 100:
    while i < n:
        word = input().lower()
        if 1 <= len(word) <= 100:
            words.append(word)
        i += 1 

for word in words:
    if len(word) <= 10:
        print(word)
    else:
        num = len(word) - 2
        print(f'{word[0]}{num}{word[-1]}')

