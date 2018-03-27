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
            print('key')
        elif operation == 'encrypt':
            print('encrypt')
        elif operation == 'decrypt':
            print('decrypt')
        elif operation == 'exit':
            break
        else:
            display_usage_message()
