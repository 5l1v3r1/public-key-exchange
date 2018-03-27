import random

from exponent import power


def create_ciphertexts(public_key, block, k):
    c1 = power(public_key[1], k, public_key[0])
    # print("(%d^%d %% %d) = %d" % (public_key[1], k, public_key[0], c1))
    
    c2 = (power(public_key[2], k, public_key[0])*(block % public_key[0])) % public_key[0]
    # print("((%d^%d %% %d)*(%d %% %d)) %% %d = %d" % (public_key[2], k, public_key[0], block, public_key[0], public_key[0], c2))

    return (c1, c2)


def decrypt(ciphertexts, private_key):
    first = power(ciphertexts[0], private_key[0]-1-private_key[2], private_key[0])
    second = ciphertexts[1] % private_key[0]
    result = first*second % private_key[0]

    return result.to_bytes(4, 'big')


def encrypt(plaintext, public_key):
    ciphertexts = []
    with open(plaintext, 'rb') as f:
        while True:
            block = f.read(4)
            if not block:
                break
            # print(block)
            block = int.from_bytes(block, 'big')

            k = random.randint(0, public_key[0]-1)

            results = create_ciphertexts(public_key, block, k)
            # print(results)
            ciphertexts.append(results[0])
            ciphertexts.append(results[1])

    return ciphertexts
