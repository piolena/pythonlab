# Lab8 - first
# Input string = 'KJGKJGKJWgHELKJGKJGUTJHFGDK'
# Print user_azos = ['G', 'G', 'G', 'H', 'G', 'G', 'U', 'T', 'H', 'G']

azos = 'HCTGU'
string = input('Input a string:')
while string != 'stop':
    user_azos = []
    for letter in string:
        if azos.find(letter) >= 0:
            user_azos.append(letter)
    print(user_azos)
    string = input('Input a string:')
