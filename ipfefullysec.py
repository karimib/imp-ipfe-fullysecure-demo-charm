from charm.toolbox.integergroup import IntegerGroup
from charm.core.math.integer import getMod, toInt
from ipfehelpers import MPK, MSK, Cy, SKx



class IPFEFULLYSEC:
    group = None
    p = None
    g = None
    h = None

    def __init__(self, sec_bits):
        self.group = IntegerGroup()
        self.group.paramgen(sec_bits)
        self.g = self.group.randomGen()
        self.h = self.group.randomGen()
        self.p = int(getMod(self.g))

    def random_vector(self, l, p):
        vector = [self.group.random() % p for _ in range(l)]
        return [int(toInt(vector[i])) for i in range(l)]

    def setup(self, l):
        si = [self.group.random() for _ in range(l)]
        ti = [self.group.random() for _ in range(l)]
        hi = [(self.g ** si[i]) * (self.h ** ti[i]) for i in range(l)]

        return MPK(self.g, self.h, hi), MSK(si, ti)

    def keygen(self, msk, x, l):
        sx = sum(int(toInt(msk.si[i])) * x[i] for i in range(l))
        tx = sum(int(toInt(msk.ti[i])) * x[i] for i in range(l)) 
        return SKx(sx, tx)

    def encrypt(self,mpk, y, l):
        r = int(toInt(self.group.random()))
        C = mpk.g ** r
        D = mpk.h ** r
        Ei = [(mpk.g ** y[i]) * (mpk.hi[i] ** r) for i in range(l)]

        return Cy(C, D, Ei)

    def decrypt(self, mpk, sk, cy, x, l):
        tmp = [int(toInt(cy.Ei[i] ** x[i])) for i in range(l)]
        res = 1
        for i in range(l):
            res *= tmp[i]

        divisor = (cy.C ** sk.sx) * (cy.D ** sk.tx)
        res /= divisor

        return res

    def get_expected_result(self, x, y, l):
        return self.g ** sum([x[i] * y[i] for i in range(l)]) % self.p
