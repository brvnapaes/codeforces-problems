string = input().lower().strip()
unique_characters = []

for char in string:
    if char not in unique_characters:
        unique_characters.append(char)

if len(unique_characters) % 2 != 0:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')