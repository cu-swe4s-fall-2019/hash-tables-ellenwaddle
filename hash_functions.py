import sys
import random


def h_ascii(key, N):  # hash fct that takes string key and hash table size
    s = 0
    if key is None or len(key) == 0:
        return 'need to specify key'
    if N is None or N < 1:
        return 'size of hash table to be > 1'
    else:
        for i in range(len(key)):
            s += ord(key[i])
        return s % N


def h_square(key, N):
    s = 0
    if key is None or len(key) == 0:
        return 'need to specify key'
    if N is None or N < 1:
        return 'size of hash table to be > 1'
    else:
        for i in range(len(key)):
            s += ord(key[i])
        s = s*s + random.randint(0, 100)
        s = s % 17 * random.randint(0,10)
        return s


def h_rolling(key, N, p=53, m=2**64):  # rolling polynomial hash
    s = 0
    if key is None or len(key) == 0:
        return 'need to specify key'
    if N is None or N < 1:
        return 'size of hash table to be > 1'
    else:
        for i in range(len(key)):
            s += ord(key[i]) * p**i
            s = s % m
        return s % N


if __name__ == '__main__':
    for l in open(sys.argv[1]):
        if sys.argv[2] == 'ascii':
            print(l, h_ascii(l, 1000))
        elif sys.argv[2] == 'rolling':
            print(l, h_rolling(l, 1000))
        elif sys.argv[2] == 'square':
            print(l, h_square(l, 1000))
