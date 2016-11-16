# Lab8 - second
# Input string = 'KJGKJGKJWGHELKJGKJGUTJHFGDK'
# Print user_azos = ['G', 'G', 'G', 'H', 'G', 'G', 'U', 'T', 'H', 'G']
#
azos = ['H', 'C', 'T', 'G', 'U']

string = input('Input a string:')
while string != 'stop':
    user_azos = list(filter(lambda letter: letter in azos, list(string)))
    print(user_azos)
    string = input('Input a string:')
