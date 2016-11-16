import random

azos = ['H', 'C', 'T', 'G', 'U']

def letter_is_azot_osn(letter):
    return letter in azos

def random_azos():
       random_index = random.randint(0, len(azos)-1)
       return azos[random_index]

def delete_by_index(list, index):
    list.pop(index)

def insert_by_index(list, index, new):
    list.insert(index, new)
