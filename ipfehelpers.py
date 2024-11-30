import random


class MPK:
    g = None
    h = None
    hi = None

    def __init__(self, g, h, hi):
        self.g = g
        self.h = h
        self.hi = hi


class MSK:
    si = None
    ti = None

    def __init__(self, si, ti):
        self.si = si
        self.ti = ti


class Cy:
    C = None
    D = None
    Ei = None

    def __init__(self, C, D, Ei):
        self.C = C
        self.D = D
        self.Ei = Ei

class SKx:
    sx = None
    tx = None

    def __init__(self, sx, tx):
        self.sx = sx
        self.tx = tx


def inner_product_mod(vector1, vector2, p):
    """
    Computes the inner product (dot product) of two vectors modulo p.

    Args:
        vector1 (list[int or float]): The first vector.
        vector2 (list[int or float]): The second vector.
        p (int): The modulus.

    Returns:
        int: The inner product of the two vectors modulo p.

    Raises:
        ValueError: If the vectors are not of the same length.
    """
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")

    # Compute the inner product modulo p
    return sum(vector1[i] * vector2[i] for i in range(len(vector1))) % p


def random_vector(low, high, n):
    """
    Generates a random vector with elements from range [a, b].

    Args:
        a (int): The lower bound (inclusive).
        b (int): The upper bound (inclusive).
        n (int): The size of the vector.

    Returns:
        list[int]: A vector (list) of random integers.
    """
    return [random.randint(low, high - 1) for _ in range(n)]
