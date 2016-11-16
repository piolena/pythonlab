'''
    Mutation partial area (10%)
'''
from mutation import *

string = input('Input a string:')
frequence = int(input('Input a frequence:'))

while string != 'stop':
    user_azos = filter(letter_is_azot_osn, list(string))
    user_azos = list(user_azos)
    print('start sequence:  ', user_azos)
    # mutate it
    area = 0
    while area < len(user_azos):
        # TODO: use frequence to count
        user_azos[area] = random_azos()
        area = area + 1
    print('mutated sequence:', user_azos)
    # get next
    string = input('Input a string:')
