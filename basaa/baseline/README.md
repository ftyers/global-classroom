# Baseline system

This is a very simple baseline system which selects the most frequent target word for each
source word and if the target word is not found it just uses the source word.

Train the system using:

```bash
$ python3 train.py ../data/train.tsv model.tsv 
Stored 14596 words
```

And apply it to the development data by doing:

```bash
$ python3 convert.py model.tsv < ../data/dev.tsv > output.tsv
```

You can then evaluate using the supplied evaluation script:

```bash
$ python3 ../evaluate.py ../data/dev.tsv output.tsv 
CER: 16.54687852515551
WER: 40.88336922205728
```
