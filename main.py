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


if __name__ == '__main__':
    test_key_exchange()
    print('All tests passed')
