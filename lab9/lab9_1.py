'''
    Mutation one area
'''
from mutation import *

string = input('Input a string:')

while string != 'stop':
    user_azos = list(filter(letter_is_azot_osn, list(string)))
    print('start sequence:  ', user_azos)
    # mutate osnovanie at area
    area = int(input('Input a area to mutate:'))
    user_azos[area] = random_azos()
    print('mutated sequence:', user_azos)

    # get next string
    string = input('Input a string:')

print('the end')
