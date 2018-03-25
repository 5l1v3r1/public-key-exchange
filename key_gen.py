from exponent import power


def create_public_keys():
    p = 11
    g = 2
    d = 3

    second = power(g, d, p)

    return (g, second, p)


def create_ciphertexts(public_keys, m, k):
    c1 = power(public_keys[0], k, public_keys[2])
    # print("(%d^%d %% %d) = %d" % (public_keys[1], k, public_keys[2], power(public_keys[1], k, public_keys[2])))
    # print("((%d^%d %% %d)*(%d %% %d)) %% %d = " % (public_keys[1], k, public_keys[2], m, public_keys[2], public_keys[2]))
    c2 = (power(public_keys[1], k, public_keys[2])*(m % public_keys[2])) % public_keys[2]

    return (c1, c2)
