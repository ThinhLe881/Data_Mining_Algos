import collections
import itertools
import sys
import math
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

    print("\nCandidate items:", len(frequent_items))

    prune_non_frequent(frequent_items, min_support)

    print("\nFrequent items:", len(frequent_items))
    '''
    print("\nFrequent items:")
    for key, value in frequent_items.items():
        print(key, ":", value)
    '''
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
    threshold = float(sys.argv[3])

    outfile = "output_apriori_" + \
        str(scale) + "_" + str(threshold) + "_" + infile
    sys.stdout = open(outfile, "w")

    with open(infile, "r") as f:
        data = f.readlines()
    baskets = []
    for line in data:
        baskets.append(list(map(int, line.split())))

    total_baskets = len(baskets)  # before scaling

    print("Total baskets:", total_baskets)

    del baskets[math.ceil(total_baskets * scale):]
    total_baskets = len(baskets)  # after scaling

    print("Scale:", scale)
    print("Total baskets after scaling:", total_baskets)

    min_support = math.ceil(total_baskets * threshold)

    print("Threshold:", threshold)
    print("Min support:", min_support)

    start_time = time.time()
    apriori(baskets, min_support)
    end_time = time.time()
    run_time = end_time - start_time

    run_time_file = "runtime_apriori_" + infile

    with open(run_time_file, "a") as f:
        f.write(outfile + ":\t\t\t\t\t" + str(run_time) + " s\n\n")


if __name__ == '__main__':
    main()
