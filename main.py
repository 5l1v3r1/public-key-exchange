def create_public_keys():
    p = 11
    g = 2
    d = 3

    second = pow(g, d) % p

    return (g, second, p)


def create_ciphertexts(public_keys, m, k):
    c1 = pow(public_keys[0], k) % public_keys[2]
    c2 = pow(public_keys[1], k)*m % public_keys[2]

    return (c1, c2)


def test_key_exchange():
    print('Testing key exchange...')
    public_keys = create_public_keys()
    assert(public_keys == (2, 8, 11))

    k = 4
    m = 7
    ciphertexts = create_ciphertexts(public_keys, m, k)
    assert(ciphertexts == (5, 6))
    print('Key exchange test passed!')


def test_decrypt():
    print('Testing decrypt...')
    ciphertexts = (5, 6)
    p = 11
    d = 3

    plaintext = pow(ciphertexts[0], p-1-d)*ciphertexts[1] % p
    assert(plaintext == 7)
    print('Decrypt test passed!')


def power(p, g, d):
    result = 1
    bits = bin(d)
    # for i in reversed(range(2, len(bits))):
    #     print(bits[i])
    for i in reversed(range(2, len(bits))):
        # print("Current bit: %d" % bits[i])
        result = result*result % p
        if int(bits[i]) == 1:
            result = result*g % p
    
    return result


def test_fast_exponentiation():
    print('Testing fast exponentiation...')
    p = 3306484913
    # p = 11
    g = 2
    d = 641361145
    # d = 3

    pub_key = power(p, g, d)
    assert(pub_key == 2990468997)
    print('Fast exponentiation test passed!')


if __name__ == '__main__':
    # test_key_exchange()
    # test_decrypt()
    test_fast_exponentiation()
    print('All tests passed')
