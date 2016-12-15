import random
from MyExceptions import *

class Sequence:
    def __init__(self):
        self.azos = ['H', 'C', 'T', 'G', 'U']

        sequence = input('Input a sequence:')
        self.user_azos = list(filter(lambda letter: letter in self.azos, list(sequence)))

    def as_str(self):
        return ''.join(self.user_azos)

    def add_random(self):
        self.user_azos.append(self.random_azos())

    def delete_first(self):
        self.user_azos.pop(0)

    def rnd_mutation(self):
        self.mutate_by_frequence(100)

    def mutation(self):
        self.mutate_by_frequence(25)

    def mutate_by_frequence(self, freq):
        mutation_count = round(len(self.user_azos) * freq / 100)
        if mutation_count == 0:
            raise MutationException("No elements to mutate, add something please")
        interval = round(len(self.user_azos) / mutation_count)
        print('all mutations: ', mutation_count, ' every ', interval, ' will mutate')
        area = 0
        while area < len(self.user_azos):
            if area % interval == 0:
                new_osn = self.random_azos()
                self.user_azos[area] = new_osn
            area = area + 1

    def random_azos(self):
        random_index = random.randint(0, len(self.azos) - 1)
        return self.azos[random_index]
