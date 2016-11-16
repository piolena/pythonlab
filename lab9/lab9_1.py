'''
    Mutation one area
'''
from mutation import *

string = input('Input a string:')

while string != 'stop':
    user_azos = filter(letter_is_azot_osn, list(string))
    user_azos = list(user_azos)
    print('start sequence:  ', user_azos)
    # mutate osnovanie at area
    area = int(input('Input a area to mutate:'))
    user_azos[area] = random_azos()
    print('mutated sequence:', user_azos)
    # get next
    string = input('Input a string:')
