# Baseline system

This is a very simple baseline system that uses a weighted finite-state transducer to try and determine
the most likely set of morphs for a particular token.

It works by using the frequency of morphs observed in the training set and trying to maximise the frequency 
of the set of morphs for new tokens.

You can train the system using:

```bash
$ python3 train.py ../data/train.tsv model.att
1719 morphemes written
```

And then use the system by running:

```bash
$ cat ../data/dev.tsv | python3 segment.py model.att > output.tsv
```

You can use the evaluation script like this:

```bash
$ python3 ../evaluate.py ../data/dev.tsv output.tsv 
10 sentences read, 77 tokens
P: 0.6406926406926408
R: 0.6331168831168831
F: 0.6352092352092351
```
