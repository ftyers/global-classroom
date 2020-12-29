# Morphological segmentation for Kʼicheʼ

Kʼicheʼ (ISO-639-3: `quc`) is a Mayan language spoken mainly in Guatemala. 


## Task


## Data

In the `data/` subdirectory you will find a training set. There is no development set, so you should
use cross-validation to set the hyperparameters of your model.

### Sample

```
Retaʼm uwach jachin xloqʼow ri pas.	R>etaʼm u>wach jachin x>loqʼow ri pas.
Na xwaj taj xinbʼij	Na x>w>a>j taj x>in>bʼi>j
Xinpaj ri nutriko.	X>in>paj ri nu>triko.
Xinta chi katulik	X>in>ta chi k>at>ul>ik
Na xwaj taj xinchʼawik	Na x>w>aj taj x>in>chʼaw>ik
Kinwaʼik rech na kinyowaj taj	K>in>waʼ>ik r>ech na k>in>yowaj taj
```

## Baseline

## Evaluation

Evaluation is F-score, that is,

<img src="https://latex.codecogs.com/gif.latex?F&space;=&space;\frac{2}{\frac{1}{P}&space;&plus;&space;\frac{1}{R}}" title="F = \frac{2}{\frac{1}{P} + \frac{1}{R}}" />

Where *P* is Precision and *R* is Recall.

## Script

The script `evaluate.py` in this repository calculates the precision, recall and F-score for
a test file. You can use it as follows:

```bash
$ python3 evaluate.py <ref_file> <tst_file>
```

The script expects the input to both files to be a two-column tab-separated file where the first column
is the input and the second column is the output of the segmenter. For example,

```bash
$ python3 evaluate.py data/test.tsv output.tsv
10 sentences read, 82 tokens
P: 0.9573170731707317
R: 0.9542682926829268
F: 0.9552845528455286
```

Where `data/test.tsv` is the test file and `output.tsv` is the output from your system.
