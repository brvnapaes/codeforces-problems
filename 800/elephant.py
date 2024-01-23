# https://codeforces.com/problemset/problem/617/A

import math

def main():
    coordinate = int(input())
    print(int(steps(coordinate)))

def steps(coordinate): 

    if coordinate > 5:
        if coordinate % 5 == 0:
            return coordinate / 5
        else:
            return math.floor((coordinate / 5) + 1)
    else:
        return 1

main()



