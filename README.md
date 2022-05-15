# Finding Frequent Itemsets Algorithms - Thinh Le

## Datasets:

-   Retail: [Link](http://fimi.uantwerpen.be/data/retail.dat)

-   Netflix: [Link](https://drive.google.com/file/d/1EX_2Pkid6EC4H-4KN0kP_S_89GKaTnXo)

## How to run:

-   Apriori:

```
python algo-name in-file scale threshold
```

e.g.

```
python apriori.py retail.dat 1 0.05
```

-   PCY, Multihash PCY, Multistage PCY:

```
python algo-name in-file scale threshold
```

e.g.

```
python pcy.py retail.dat 1 0.05
```

-   Random Sampling Apriori:

```
python algo-name in-file scale sample-size threshold
```

e.g.

```
python rs_apriori.py retail.dat 1 0.1 0.05
```

-   Random Sampling Apriori:

```
python algo-name in-file scale sample-size threshold
```

e.g.

```
python son_apriori.py retail.dat 1 0.2 0.05
```
