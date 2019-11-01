import hash_functions
import sys
import time
import random


def reservoir_sampling(new_val, size, V):
    if len(V) < size:
        V.append(new_val)
    else:
        j = random.randint(0, len(V))
        if j < len(V):
            V[j] = new_val


class LinearProbe:
    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [None for i in range(N)]
        self.M = 0

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] is None:
                self.T[test_slot] = (key, value)
                self.M += 1
                return True
        return False

    def search(self, key):
        start_hash = self.hash_function(key, self.N)

        for i in range(self.N):
            test_slot = (start_hash + i) % self.N
            if self.T[test_slot] is None:
                return None
            if self.T[test_slot][0] == key:
                return self.T[test_slot][1]
        return None


class ChainedHash:
    keys = []

    def __init__(self, N, hash_function):
        self.hash_function = hash_function
        self.N = N
        self.T = [[] for i in range(N)]
        self.M = 0

    def add(self, key, value):
        start_hash = self.hash_function(key, self.N)
        self.T[start_hash] = self.hash(key, self.N)
        self.M += 1
        keys=keys.append(key)  #store the set of keys stored in hash table
        return True

    def search(self, key):
        start_hash = self.hash_function(key, self.N)

        for k, v in self.T[start_hash]:
            if key == k:
                return v
        return None


if __name__ == '__main__':
    N = int(sys.argv[1])
    hash_alg = 'rolling'  # ascii, rolling, or square
    collision_strategy = sys.argv[3]  # linear or chain
    data_file_name = sys.argv[4]
    keys_to_add = int(sys.argv[5])

    ht = None

    if collision_strategy == 'linear':
        ht = LinearProbe(N, hash_functions.h_rolling)
    elif collision_strategy == 'chain':
        ht = ChainHash(N, hash_functions.h_rolling)

    keys_to_search = 100
    V = []

    for l in open(data_file_name):
        reservoir_sampling(l, keys_to_search, V)
        t0 = time.time()
        ht.add(l, l)
        t1 = time.time()
        print('insert', ht.M/ht.N, t1 - t0)
        if ht.M == keys_to_add:
            break

    for v in V:
        t0 = time.time()
        r = ht.search(v)
        t1 = time.time()
        print('search', t1 - t0)
