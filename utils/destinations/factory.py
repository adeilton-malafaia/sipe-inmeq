import random
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 890), randint(473, 573)


fake = Faker('pt_BR')


def makeSaida():
    destino = ['d', 'i', 'r']
    num_words = random.choice([1, 2, 3])
    num_dig_qn = random.choice([2, 3, 4, 5])
    unid = random.choice(['g', 'kg', 'mm', 'cm', 'm', 'Un.'])
    return {
        'data': fake.date(),
        'tc': fake.random_number(digits=7, fix_len=True),
        'destino': random.choice(destino),
        'produto': fake.sentence(nb_words=num_words),
        'marca': fake.sentence(nb_words=num_words),
        'qn': str(fake.random_number(digits=num_dig_qn, fix_len=True)) + unid,
        'quant': random.choice([5, 13, 20, 32, 80])
    }
