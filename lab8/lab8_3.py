# Lab8 - third
# Input string = 'KJGKJGKJWGHELKJGKJGUTJHFGDK'
# Print user_azos = ['G', 'G', 'G', 'H', 'G', 'G', 'U', 'T', 'H', 'G']
#
def letter_is_azot_osn(letter):
    return letter in ['H', 'C', 'T', 'G', 'U']


string = input('Input a string:')
while string != 'stop':
    user_azos = list(filter(letter_is_azot_osn, list(string)))
    print(user_azos)
    string = input('Input a string:')
