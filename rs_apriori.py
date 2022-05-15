import collections
import itertools
import sys
import math
import random
import time


def prune_non_frequent(set_k, min_support):
    for key, value in list(set_k.items()):
        if value < min_support:
            del set_k[key]


def apriori(baskets, min_support):
    frequent_items = collections.defaultdict(int)

    for basket in baskets:
        for element in basket:
            frequent_items[element] += 1

    prune_non_frequent(frequent_items, min_support)

    frequent_pairs = collections.defaultdict(int)

    for basket in baskets:
        items = []
        pairs = []
        for item in basket:
            if item in frequent_items:
                items.append(item)
        pairs = list(itertools.combinations(items, 2))
        for pair in pairs:
            frequent_pairs[pair] += 1

    prune_non_frequent(frequent_pairs, min_support)

    return frequent_pairs


def rs_apriori(baskets, threshold, sample_size):
    total_baskets = len(baskets)
    min_support = math.ceil(total_baskets * threshold)

    print("Min support:", min_support)
    print("Random sample size:", sample_size)

    cut = math.ceil(total_baskets * sample_size)
    random.shuffle(baskets)
    sample_baskets = baskets[:cut]
    remaining_baskets = baskets[cut:]

    total_sample_baskets = len(sample_baskets)
    sample_min_support = math.ceil(total_sample_baskets * threshold * 0.9)

    print("\nTotal baskets after random sampling:", total_sample_baskets)
    print("Min support of sample:", sample_min_support)

    frequent_pairs = apriori(sample_baskets, sample_min_support)

    frequent_items = set(itertools.chain(*list(frequent_pairs.keys())))

    for basket in remaining_baskets:
        items = []
        pairs = []
        for item in basket:
            if item in frequent_items:
                items.append(item)
        pairs = list(itertools.combinations(items, 2))
        for pair in pairs:
            if pair in frequent_pairs:
                frequent_pairs[pair] += 1

    print("\nCandidate pairs:", len(frequent_pairs))

    prune_non_frequent(frequent_pairs, min_support)

    print("\nFrequent pairs:", len(frequent_pairs))
    '''
    print("\nFrequent pairs:")
    for key, value in frequent_pairs.items():
        print(key, ":", value)
    '''


def main():
    infile = sys.argv[1]
    scale = float(sys.argv[2])
    sample_size = float(sys.argv[3])
    threshold = float(sys.argv[4])

    outfile = "output_rs_apriori_" + str(scale) + "_" + str(sample_size) + "_" + \
        str(threshold) + "_" + infile
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
    print("Threshold:", threshold)

    start_time = time.time()
    rs_apriori(baskets, threshold, sample_size)
    end_time = time.time()
    run_time = end_time - start_time

    run_time_file = "runtime_rs_apriori_" + infile

    with open(run_time_file, "a") as f:
        f.write(outfile + ":\t\t\t\t\t" + str(run_time) + " s\n\n")


if __name__ == '__main__':
    main()
