import random

from exponent import power
from prime import generate_random_prime


def set_up_keys():
    p = generate_random_prime(32)
    g = make_generator()

    print('Generating private keys...\n')
    d = create_private_keys(p, g)
    print('Generating public keys...\n')
    create_public_keys(p, g, d)

    
def create_private_keys(p, g):
    d = random.randint(1, p-1)

    print('\nPrivate keys:')
    print('p = %d' % p)
    print('g = %d' % g)
    print('d = %d' % d)

    priv_file = open('testfiles/privkey.txt', 'w')

    line = ' '.join(str(key) for key in [p, g, d])
    line = line + '\n'
    priv_file.write(line)

    priv_file.close()

    return d


def create_public_keys(p, g, d):
    e2 = power(g, d, p)
    print('\nPublic keys:')
    print('p = %d' % p)
    print('g = %d' % g)
    print('e2 = %d' % e2)
    print('\n')

    pub_file = open('testfiles/pubkey.txt', 'w')

    line = ' '.join(str(key) for key in [p, g, e2])
    line = line + '\n'
    pub_file.write(line)

    pub_file.close()


def make_generator():
    return 2
