'''
    Mutation partial area (e.g. 10%)
'''
from mutation import *

string = input('Input a string:')
frequence = int(input('Input a frequence,%:'))

while string != 'stop':
    user_azos = list(filter(letter_is_azot_osn, list(string)))
    print('start sequence:  ', user_azos)
    # mutate some
    mutate_by_frequence(user_azos, frequence)
    print('mutated sequence:', user_azos)
    # get next
    string = input('Input a string:')
