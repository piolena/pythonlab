'''
    Delete one area
'''
from mutation import *

string = input('Input a string:')

while string != 'stop':
    user_azos = filter(letter_is_azot_osn, list(string))
    user_azos = list(user_azos)
    print('start sequence:  ', user_azos)
    # delete osnovanie at area
    area = int(input('Input a area to delete:'))
    delete_by_index(user_azos, area)
    print('updated sequence:', user_azos)
    # get next
    string = input('Input a string:')
