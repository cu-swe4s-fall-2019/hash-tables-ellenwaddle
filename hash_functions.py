import sys

def h_ascii(key, N):  #hash fct that takes string key and hash table size
    s = 0
    if key is None or len(key)==0:
        return 'need to specify key'
    if N is None or N < 1:
        return 'size of hash table has to be at least 1'
    else:
        for i in range(len(key)):
            s += ord(key[i])
        return s % N

def h_square(key, N):
    s = 0
    if key is None or len(key)==0:
        return 'need to specify key'
    if N is None or N < 1:
        return 'size of hash table must be at least 1'
    else:
        for i in range(len(key)):
            s += ord(key[i])
        s = s*s - rand.random(0,100)
        return s

def h_rolling(key, N, p=53, m=2**64): #rolling polynomial hash
    s = 0
    if key is None or len(key)==0:
        return 'need to specify key'
    if N is None or N < 1:
        return 'size of hash table has to be at least 1'
    else:
        for i in range(len(key)):
            s += ord(key[i]) * p**i
            s = s % m
        return s % N
