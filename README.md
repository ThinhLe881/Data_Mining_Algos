# Finding Frequent Itemsets Algorithms - Thinh Le

## Datasets:

### Retail: [Link](http://fimi.uantwerpen.be/data/retail.dat)

### Netflix: [Link](https://drive.google.com/file/d/1EX_2Pkid6EC4H-4KN0kP_S_89GKaTnXo)

## How to run:

### Apriori:

**python _algo-name_ _in-file_ _scale_ _threshold_**
e.g. **python apriori.py retail.dat 1 0.05**

### PCY, Multihash PCY, Multistage PCY:

**python _algo-name_ _in-file_ _scale_ _threshold_**
e.g. **python pcy.py retail.dat 1 0.05**

### Random Sampling Apriori:

**python _algo-name_ _in-file_ _scale_ _sample-size_ _threshold_**
e.g. **python rs_apriori.py retail.dat 1 0.1 0.05**

### Random Sampling Apriori:

**python _algo-name_ _in_file_ _scale_ _sample-size_ _threshold_**
e.g. **python son_apriori.py retail.dat 1 0.2 0.05**
