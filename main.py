import random

from crypt import *
from key_gen import *


def display_usage_message():
    print('\n')
    print('Usage:')
    print('\'key_gen\'  Generates a new public and private key (saved as pubkey.txt and privkey.txt respectively under testfiles/')
    print('\'encrypt\'  Encrypts plaintext into blocks of ciphertext (assumes plaintext exists as ptext.txt and saves output as ctext.txt both under testfiles/')
    print('\'decrypt\'  Decrypts blocks of ciphertext into plaintext (assumes ciphertext exists as ctext.txt and saves output as dtext.txt both under testfiles/')
    print('\'exit\'     Exit the program')
    print('\n')


if __name__ == '__main__':
    while True:
        operation = input('Enter a command: ')
        if operation == 'key_gen':
            seed = input('Input a seed: ')
            seed = random.seed(int(seed))
            set_up_keys()
        elif operation == 'encrypt':
            with open('testfiles/pubkey.txt', 'r') as f:
                public_key = f.readline().rsplit()
                public_key = [int(num) for num in public_key]
                ciphertexts = encrypt('testfiles/ptext.txt', public_key)
                print('Ciphertext:')
                print(ciphertexts)
        elif operation == 'decrypt':
            with open('testfiles/privkey.txt', 'r') as f:
                private_key = f.readline().rsplit()
                private_key = [int(num) for num in private_key]

            plaintext = decrypt('testfiles/ctext.txt', private_key)
            print('Plaintext')
            print(plaintext)
        elif operation == 'exit':
            break
        else:
            display_usage_message()
