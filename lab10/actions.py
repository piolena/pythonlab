import random

azos = ['H', 'C', 'T', 'G', 'U']

def add_random(list):
    list.append(random_azos())
    return ''.join(list)

def delete_first(list):
    list.pop(0)
    return ''.join(list)

def mutation(list):
    mutate_by_frequence(list, 100)
    return ''.join(list)

def rnd_mutation(list):
    mutate_by_frequence(list, 25)
    return ''.join(list)

def letter_is_azot_osn(letter):
    return letter in azos

def random_azos():
       random_index = random.randint(0, len(azos)-1)
       return azos[random_index]

def mutate_by_frequence(list, freq):
    mutation_count = round(len(list) * freq / 100)
    interval = round(len(list) / mutation_count)
    print('all mutations: ', mutation_count, ' every ', interval, ' will mutate')
    area = 0
    while area < len(list):
        if area % interval == 0:
            new_osn = random_azos()
            list[area] = new_osn
        area = area + 1

