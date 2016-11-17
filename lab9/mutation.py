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


def mutate_by_frequence(list, freq):
    mutation_count = int(len(list) * freq / 100)
    far = int(len(list) / mutation_count)
    print('all mutations: ', mutation_count, ' every ', far, ' will mutate')
    area = 0
    while area < len(list):
        if area % far == 0:
            new_osn = random_azos()
            print('mutation number ', area, ' was ', list[area], ' mutate to ', new_osn)
            list[area] = new_osn
        area = area + 1

