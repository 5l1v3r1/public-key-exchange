Name: Grant Lindberg
Date: March 23, 2018
Project: Program 2

Description: A secret key exchange program that allows a user to create both public keys and private keys, encrypt plaintext, and decrypt ciphertext.

How to build/run:

Please have Python3 installed before using.

Type 'python3 main.py'

User commands are described below.

User commands:

'key_gen': Prompts the user to seed a number. Generates a private key saved under testfiles/privkey.txt and public key saved under testfiles/pubkey.txt.
'encrypt': Reads plaintext from 'testfiles/ptext.txt' and encrypts it to ciphertext, which will be saved as pairs of integers in 'testfiles/ctext.txt'.
'decrypt': Reads ciphertext from 'testfiles/ctext.txt' and encrypts it to plaintext, which will be saved as bytes in 'testfiles/ptext.txt'.
'exit': Exits the program.

The user will receive a usage message if he/she enters an incorrect command.

Included files:

main.py - The driver code for the program. Prompts the user for inputs, including key generation, encryption, and decryption
key_gen.py - This files creates both the public and private keys for the user
prime.py - Generates the random prime values for key generation using the Miller-Rabin algorithm
exponent.py - Performs fast exponentiation using the square-and-multiply algorithm
crypt.py - Handles both encryption and decryption

NOTES: Please make sure that 'ptext.txt' exists before encrypting and 'ctext.txt' exists before decrypting. This program will be able to handle encrypting variable-length inputs; however, please make sure there are no carriage returns in your test files i.e. please use POSIX-compliant files, or you will be unable to interpret the output. This program ONLY handles ascii characters.
