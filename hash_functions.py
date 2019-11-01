import sys
import random


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

#if __name__ == '__main__':
#    for l in open(sys.argv[1]):

#        print(l, h_rolling(l, 1000))
