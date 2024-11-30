import random
from charm.toolbox.pairinggroup import PairingGroup, G1
from ipfehelpers import random_vector, MPK, MSK, Cy, inner_product_mod, SKx


group = PairingGroup("SS512")
g = group.random(G1)
h = group.random(G1)
p = group.order()

l = 5


def setup(l):
    s = random_vector(0, p, l)
    t = random_vector(0, p, l)
    hi = [(g ** s[i]) * (h ** t[i]) for i in range(l)]

    return MPK(g, h, hi), MSK(s, t)


def keygen(msk, x):
    sx = inner_product_mod(msk.si, x, p)
    tx = inner_product_mod(msk.ti, x, p)
    return SKx(sx, tx)


def encrypt(mpk, y):
    r = random.randint(0, p)
    C = mpk.g**r
    D = mpk.h**r
    Ei = [(mpk.g ** y[i]) * (mpk.hi[i] ** r) for i in range(l)]

    return Cy(C, D, Ei)


def decrypt(mpk, sk, cy, x):
    res = 1
    for i in range(l):
        res *= (cy.Ei[i] ** x[i])

    divisor = (cy.C**sk.sx) * (cy.D**sk.tx)
    res /= divisor

    return res


def find_dlog(g, h):
    for i in range(1, p):
        if g**i == h:
            return i

    return -1


def main():
    mpk, msk = setup(l)
    x = random_vector(0, p, l)
    sk = keygen(msk, x)
    y = random_vector(0, p, l)
    cy = encrypt(mpk, y)
    res = decrypt(mpk, sk, cy, x)
    # This is computationally expensive
    # val = find_dlog(g, res)

    expected = inner_product_mod(x, y, p)
    print("<x,y> ", expected)
    print("g^<x,y>: ", g**expected)
    # print("Dlog result: ", val)
    print("Decrypted result: ", res)


main()
