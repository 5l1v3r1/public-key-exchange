def to_bin_array(bits):
    array = []
    bits = bits[2:]
    # print(bits)
    for bit in bits:
        array.append(int(bit))

    return array


def power(base, exponent, modulus):
    result = 1
    bits = bin(exponent)
    bits = to_bin_array(bits)
    # print(bits)
    for bit in bits:
        result = result*result % modulus
        if bit == 1:
            result = result*base % modulus
    
    return result


def fast_pow(base, exponent):
    result = 1
    for _ in range(0, exponent):
        result *= base

    return result
