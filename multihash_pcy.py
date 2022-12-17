import collections
import bitarray
import itertools
import sys
import math
import time
import argparse


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
    N = 50021

    frequent_items = collections.defaultdict(int)
    buckets_1 = collections.defaultdict(int)
    buckets_2 = collections.defaultdict(int)

    for basket in baskets:
        for item in basket:
            frequent_items[item] += 1
        pairs = list(itertools.combinations(basket, 2))
        for pair in pairs:
            index_1 = hash_1(pair[0], pair[1], N)
            index_2 = hash_2(pair[0], pair[1], N)
            buckets_1[index_1] += 1
            buckets_2[index_2] += 1

    bitmap_1 = N * bitarray.bitarray('0')
    bitmap_2 = N * bitarray.bitarray('0')

    for key, count in buckets_1.items():
        if count >= min_support:
            bitmap_1[key] = 1

    for key, count in buckets_2.items():
        if count >= min_support:
            bitmap_2[key] = 1

    print("\nCandidate items:", len(frequent_items))

    prune_non_frequent(frequent_items, min_support)

    print("\nFrequent items:", len(frequent_items))
    '''
    print("\nFrequent items:")
    for key, value in frequent_items.items():
        print(key, ":", value)
    '''
    frequent_pairs = collections.defaultdict(int)

    count = 0
    for basket in baskets:
        items = []
        pairs = []
        for item in basket:
            if item in frequent_items:
                items.append(item)
        pairs = list(itertools.combinations(items, 2))
        for pair in pairs:
            if pair in frequent_pairs:
                frequent_pairs[pair] += 1
            elif (bitmap_1[hash_1(pair[0], pair[1], N)] == 1) and (bitmap_2[hash_2(pair[0], pair[1], N)] == 1):
                frequent_pairs[pair] += 1

    print("\nCandidate pairs:", len(frequent_pairs))

    prune_non_frequent(frequent_pairs, min_support)

    print("\nFrequent pairs:", len(frequent_pairs))

    print("\nFrequent pairs:")
    for key, value in frequent_pairs.items():
        print(key, ":", value)


def main():
    parser = argparse.ArgumentParser(description='Multi-hash PCY Algorithm')
    parser.add_argument('infile', metavar='infile', type=str, help='The input dataset (.txt, .dat, .data)')
    parser.add_argument('scale', metavar='scale', type=str, help='The scale of the dataset (eg. 0.1 for 10%, 1 for the entire dataset)')
    parser.add_argument('threshold', metavar='threshold', type=str, help='The threshold (eg. 0.01 for 1%)')
    args = parser.parse_args()

    infile = args.infile
    scale = float(args.scale)
    threshold = float(args.threshold)

    outfile = "output_multihash_pcy_" + \
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

    run_time_file = "runtime_multihash_pcy_" + infile

    with open(run_time_file, "a") as f:
        f.write(outfile + ":\t\t\t\t\t" + str(run_time) + " s\n\n")


if __name__ == '__main__':
    main()
