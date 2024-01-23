limak, bob = input().split(' ')
limak = int(limak)
bob = int(bob)
years = 0

while limak <= bob :
    limak = limak * 3
    bob = bob * 2
    years += 1

print(years)