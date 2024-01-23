# https://codeforces.com/problemset/problem/339/A

s = input().split('+')
ones=[]
twos=[]
threes=[]
sum = ''

length = len(s)

for num in s:
    if num == '1':
        ones.append(num)
    elif num == '2':
        twos.append(num)
    elif num =='3':
        threes.append(num)

for num in ones:
    sum += num + '+'

for num in twos:
    sum += num + '+'

for num in threes:
    sum += num + '+'

print(sum[:-1])