from exponent import power


def create_public_keys(private_key):
    e2 = power(private_key[1], private_key[2], private_key[0])

    return (private_key[0], private_key[1], e2)


def make_generator():
    return 2
