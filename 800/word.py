# https://codeforces.com/problemset/problem/59/A

word = list(input())
lower = []
upper = []

for char in word:
    if char.islower():
        lower.append(char)
    elif char.isupper():
        upper.append(char)

word = map(str, word)
word = ''.join(word)

if len(lower) >= len(upper):
    print(word.lower())
else:
    print(word.upper())

