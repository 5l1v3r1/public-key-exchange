import random


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
    for i in reversed(range(2, len(bits))):
        result = result*result % p
        if int(bits[i]) == 1:
            result = result*g % p
    
    return result


def test_fast_exponentiation():
    print('Testing fast exponentiation...')
    p = 3306484913
    g = 2
    d = 641361145

    pub_key = power(p, g, d)
    assert(pub_key == 2990468997)
    print('Fast exponentiation test passed!')


def find_integers_for_prime_testing(n):
    # n >= 3
    q = (n-1)
    k = 0
    while True:
        q = q // 2
        k += 1
        if q % 2 == 1:
            return (k, q)

    return (-1, -1)


def is_prime(n):
    if n == 2:
        return True
    (k, q) = find_integers_for_prime_testing(n)
    a = random.randint(2, n-2)
    print("n: %d" % n)
    print("k: %d" % k)
    print("q: %d" % q)
    print("a: %d" % a)
    if pow(a, q) % n == 1:
        return True
    for j in range(0, k-1):
        if pow(a, pow(2, j)*q) % n == n-1:
            return True

    return False


def test_miller_rabin():
    print('Testing Miller-Rabin...')
    # assert(is_prime(104717))
    # assert(is_prime(577757))
    # assert(is_prime(101089))
    assert(is_prime(280001))
    # assert(not is_prime(95721889))
    # assert(not is_prime(4096))
    # assert(not is_prime(252601))
    # assert(not is_prime(3057601))
    print('Miller-Rabin test passed!')


if __name__ == '__main__':
    # test_key_exchange()
    # test_decrypt()
    # test_fast_exponentiation()
    test_miller_rabin()
    print('All tests passed')
