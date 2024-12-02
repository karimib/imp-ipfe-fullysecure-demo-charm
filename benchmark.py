import time
import csv
from ipfefullysec import IPFEFULLYSEC

l = 5

stages = [512, 1024]

def test():
    G = IPFEFULLYSEC(512)
    mpk, msk = G.setup(l)
    x = G.random_vector(l, G.p)
    skx = G.keygen(msk, x, l)
    y = G.random_vector(l, G.p)
    cy = G.encrypt(mpk, y, l)
    res = G.decrypt(mpk, skx, cy, x, l)
    # This is computationally expensive
    # val = find_dlog(g, res)

    expected = sum([x[i] * y[i] for i in range(l)])
    print("<x,y> ", expected)
    print("g^<x,y>: ", G.g**expected)
    # print("Dlog result: ", val)
    print("Decrypted result: ", res)


## Tests 
def simulate_increasing_bits():
    results = []
    for bits in stages:
        G = IPFEFULLYSEC(bits)

        x = G.random_vector(l, G.p)
        y = G.random_vector(l, G.p)

        start_time = time.time()
        mpk, msk = G.setup(l)
        setup_time = time.time() - start_time

        start_time = time.time()
        skx = G.keygen(msk, x, l)
        keygen_time = time.time() - start_time

        start_time = time.time()
        cy = G.encrypt(mpk, y, l)
        encrypt_time = time.time() - start_time

        start_time = time.time()
        v = G.decrypt(mpk, skx, cy, x, l)
        decrypt_time = time.time() - start_time

        setup_time *= 1_000_000_000
        keygen_time *= 1_000_000_000
        encrypt_time *= 1_000_000_000
        decrypt_time *= 1_000_000_000
        total_time = setup_time + keygen_time + encrypt_time + decrypt_time

        print("bits: ", bits)

        results.append([bits, l, setup_time, encrypt_time, keygen_time, decrypt_time, total_time])

    with open('data/ipfe-fullysec_timings_increasing_bits.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['bits', 'l', 'time setup', 'time encrypt', 'time keygen', 'time decrypt', 'time total'])
        csvwriter.writerows(results)


def simulate_increasing_l():
    results = []
    bits = 512
    length = [100, 1000, 10000]
    G = IPFEFULLYSEC(bits)
    
    for l in length:
        x = G.random_vector(l, G.p)
        y = G.random_vector(l, G.p)

        start_time = time.time()
        mpk, msk = G.setup(l)
        setup_time = time.time() - start_time

        start_time = time.time()
        skx = G.keygen(msk, x, l)
        keygen_time = time.time() - start_time

        start_time = time.time()
        cy = G.encrypt(mpk, y, l)
        encrypt_time = time.time() - start_time

        start_time = time.time()
        v = G.decrypt(mpk, skx, cy, x, l)
        decrypt_time = time.time() - start_time

        setup_time *= 1_000_000_000
        keygen_time *= 1_000_000_000
        encrypt_time *= 1_000_000_000
        decrypt_time *= 1_000_000_000
        total_time = setup_time + keygen_time + encrypt_time + decrypt_time

        print("bits: ", bits)

        results.append([bits, l, setup_time, encrypt_time, keygen_time, decrypt_time, total_time])

    with open('data/ipfe-fullysec_timings_increasing_l.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['bits', 'l', 'time setup', 'time encrypt', 'time keygen', 'time decrypt', 'time total'])
        csvwriter.writerows(results)


simulate_increasing_l()