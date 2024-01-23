# https://codeforces.com/problemset/problem/112/A

def main():
    str1 = list(input().lower())
    str2 = list(input().lower())

    is_equal(str1, str2)

def is_equal(str1, str2):

    if str1 == str2:
        print('0')
        return
    
    length = len(str1)
    
    for i in range(length):
        if str1[i] != str2[i]:
            dif1 = str1[i]
            dif2 = str2[i]
            break

    if dif1 > dif2:
        print('1')
    else:
        print('-1')

main()
