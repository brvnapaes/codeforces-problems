n = int(input())
colors = input()
remove = 0
 
for i in range(n-1):
    if colors[i] == colors[i+1]:
        remove += 1
 
print(remove)