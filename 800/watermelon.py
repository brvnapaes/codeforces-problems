try:
    weight = int(input())

    if 1 <= weight <= 100 and weight != 2:
        if (weight % 2 == 0):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

except ValueError:
    print('NO')
