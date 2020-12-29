# Predictive text for Chukchi

Chukchi (*Ԓыгъоравэтԓьэн*; ISO-639-3: `ckt`) is a language spoken in Chukotka Autonomous Okrug in the north-east of Siberia.

## Task

Next unit prediction is the task of given an input sequence predicting the next element in the sequence. For example
given the input sequence [to, be, or, not] we would expect the next two elements to be [to, be] respectively. The 
units of prediction may be words, characters or some other sub-word unit.

In most predictive keyboards, the unit of prediction is the word, however in a language like Chukchi, where words
may consist of many morphs, this is likely not the most appropriate unit. Consider the sentence *иаʼмэ майӈывэтгавыркынэтык ынӄэн нэгитэркынитык* "why 
are you speaking so loudly, they are looking at you" 

| Chukchi | Segmentation | Gloss | Translation |
|---------|--------------|-------|-------------|
| иаʼмэ   | `иа'м>э`     | `why-EMPH` | Why so |
| майӈывэтгавыркынэтык | `майӈы>вэтгавы>ркынэ>тык` | `loudly-speak-IMPF-2PL.S` | loudly do you speak? |
| ынӄэн | `ынӄэн` | `DISC` | -- |
| нэгитэркынитык | `нэ>гитэ>ркыни>тык` | `3PL.S-watch-IMPF-2PL.O` | they are looking at you |

As you can see, much of the information that is expressed with words in English is expressed with morphs in Chukchi.

## Data

In the `data/` subdirectory you will find a training set and a development set. 

### Sample

```
амаравкэваратэн таа’койӈын	а>маравкэва>ра>тэн таа>’ко>йӈы>н
йъйыӄык ныӄэԓпэратӄэн вытэчгытрыӄэргыԓьын йыӈэттэт	йъйыӄы>к ны>ӄэԓпэр>ат>ӄэн вытэч>гытры>ӄэргы>ԓьы>н йыӈэт>тэ>т
мыкыӈ нывытрэтӄин чеԓгатвытрыԓьо ынӄорыым вытэчгытрыԓьо	мык>ы>ӈ ны>вытрэт>ӄин чеԓг>ат>вытры>ԓь>о ынӄор>ыым вытэч>гытры>ԓь>о
ынӄорыым ныӄэргавыӈоӄэн нычеԓгъав	ынӄор>ыым ны>ӄэргав>ыӈо>ӄэн ны>чеԓ>гъа>в
```

## Baseline

The baseline is a simple model that predicts the next word based on the previous word.

## Evaluation

The idea of the project is to reduce the number of clicks a user has to make to a minimum, so the evaluation
will be the average number of clicks per sentence on the test corpus. 
