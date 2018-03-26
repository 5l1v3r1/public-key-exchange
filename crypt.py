import struct

from exponent import power

def decrypt(ciphertexts, private_key):
    first = power(ciphertexts[0], private_key[0]-1-private_key[2], private_key[0])
    second = ciphertexts[1] % private_key[0]
    result = first*second % private_key[0]

    return result.to_bytes(4, 'big')
