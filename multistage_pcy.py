import collections
import itertools
import bitarray
import sys
import math
import time


def hash_1(a, b, N):
    return (a * 7 + 11 * b) % N


def hash_2(a, b, N):
    # Cantor pairing function
    return int(((((a + b) * (a + b + 1)) / 2) + a) % N)


def prune_non_frequent(set_k, min_support):
    for key, value in list(set_k.items()):
        if value < min_support:
            del set_k[key]


def pcy(baskets, min_support):
    N_1 = 100003
    N_2 = 50021

    frequent_items_1 = collections.defaultdict(int)
    buckets_1 = collections.defaultdict(int)

    for basket in baskets:
        for item in basket:
            frequent_items_1[item] += 1
        pairs = list(itertools.combinations(basket, 2))
        for pair in pairs:
            index = hash_1(pair[0], pair[1], N_1)
            buckets_1[index] += 1

    bitmap_1 = N_1 * bitarray.bitarray('0')

    for key, count in buckets_1.items():
        if count >= min_support:
            bitmap_1[key] = 1

    print("\nCandidate items:", len(frequent_items_1))

    prune_non_frequent(frequent_items_1, min_support)

    print("\nFrequent items:", len(frequent_items_1))
    '''
    print("\nFrequent items:")
    for key, value in frequent_items_1.items():
        print(key, ":", value)
    '''
    frequent_pairs_1 = list(itertools.combinations(frequent_items_1, 2))
    frequent_pairs_1 = set(
        [pair for pair in frequent_pairs_1 if bitmap_1[hash_1(pair[0], pair[1], N_1)] == 1])

    print("\nCandidate pairs in Pass 2:", len(frequent_pairs_1))

    frequent_items_2 = set(itertools.chain(*frequent_pairs_1))
    buckets_2 = collections.defaultdict(int)

    for basket in baskets:
        items = []
        pairs = []
        for item in basket:
            if item in frequent_items_2:
                items.append(item)
        pairs = list(itertools.combinations(items, 2))
        for pair in pairs:
            if pair in frequent_pairs_1:
                index = hash_2(pair[0], pair[1], N_2)
                buckets_2[index] += 1

    bitmap_2 = N_2 * bitarray.bitarray('0')

    for key, count in buckets_2.items():
        if count >= min_support:
            bitmap_2[key] = 1

    frequent_pairs_2 = collections.defaultdict(int)

    for basket in baskets:
        items = []
        pairs = []
        for item in basket:
            if item in frequent_items_2:
                items.append(item)
        pairs = list(itertools.combinations(items, 2))
        for pair in pairs:
            if pair in frequent_pairs_2:
                frequent_pairs_2[pair] += 1
            elif (pair in frequent_pairs_1) and (bitmap_2[hash_2(pair[0], pair[1], N_2)] == 1):
                frequent_pairs_2[pair] += 1

    print("\nCandidate pairs:", len(frequent_pairs_2))

    prune_non_frequent(frequent_pairs_2, min_support)

    print("\nFrequent pairs:", len(frequent_pairs_2))
    '''
    print("\nFrequent pairs:")
    for key, value in frequent_pairs_2.items():
        print(key, ":", value)
    '''


def main():
    infile = sys.argv[1]
    scale = float(sys.argv[2])
    threshold = float(sys.argv[3])

    outfile = "output_multistage_pcy_" + \
        str(scale) + "_" + str(threshold) + "_" + infile
    sys.stdout = open(outfile, "w")

    with open(infile, "r") as f:
        data = f.readlines()
    baskets = []
    for line in data:
        baskets.append(list(map(int, line.split())))

    total_baskets = len(baskets)  # before scaling

    print("Total baskets:", total_baskets)

    del baskets[math.ceil(total_baskets*scale):]
    total_baskets = len(baskets)  # after scaling

    print("Scale:", scale)
    print("Total baskets after scaling:", total_baskets)

    min_support = math.ceil(total_baskets * threshold)

    print("Threshold:", threshold)
    print("Min support:", min_support)

    start_time = time.time()
    pcy(baskets, min_support)
    end_time = time.time()
    run_time = end_time - start_time

    run_time_file = "runtime_multistage_pcy_" + infile

    with open(run_time_file, "a") as f:
        f.write(outfile + ":\t\t\t\t\t" + str(run_time) + " s\n\n")


if __name__ == '__main__':
    main()
