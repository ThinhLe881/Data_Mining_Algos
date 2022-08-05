# Frequent Itemsets Mining - Thinh Le

## Datasets:

-   **Retail:** [Link](http://fimi.uantwerpen.be/data/retail.dat)
    -   Over 500000 items from over 88000 users

-   **Netflix:** [Link](https://drive.google.com/file/d/1EX_2Pkid6EC4H-4KN0kP_S_89GKaTnXo)
    -   Over millions items from over 480000 users

## How to run:

-   **Apriori:**

```
python algo-name in-file scale threshold
```

_e.g._

```
python apriori.py retail.dat 1 0.05
```

-   **PCY, Multihash PCY, Multistage PCY:**

```
python algo-name in-file scale threshold
```

_e.g._

```
python pcy.py retail.dat 1 0.05
```

-   **Random Sampling Apriori:**

```
python algo-name in-file scale sample-size threshold
```

_e.g._

```
python rs_apriori.py retail.dat 1 0.1 0.05
```

-   **SON Apriori:**

```
python algo-name in-file scale sample-size threshold
```

_e.g._

```
python son_apriori.py retail.dat 1 0.2 0.05
```
