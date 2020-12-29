
# Tone prediction and orthographic conversion for Basaa

Basaa (*Ɓàsàa*; ISO-639-3: `bas`) is a Bantu language spoken in Cameroon. It is a tonal language. The language has several orthographies, two are "missionary" orthographies and another is [an orthography](https://en.wikipedia.org/wiki/General_Alphabet_of_Cameroon_Languages) supported by the Academy of Languages of Cameroon.

| Academy | Missionary (Protestant) | Missionary (Catholic) |
|---------|-------------------------|-----------------------|
| Mɛ̀ yè lɛ mɛ̀ ɓɔl nyɔɔ̄ nı̀ màkòò. | Me yé le me bol nyoo ni makôô. | Mè ye lè mè bòl nyòò ni makoo. |

As you can see from the example, the Academy orthography writes the tones, where the two missionary orthographies do not. 

## Task

The purpose of this task is to create a system that will, given input in the missionary orthography convert it to the academy orthography. 

## Data

In the `data/` subdirectory you will find a training set and a development set. The files are tab-separated, in the first column is the Academy orthography and in the second column is the protestant missionary orthography.

| File | Sentences | Tokens |
|------|-----------|--------|
| `train.tsv` | 10000 | 113628 |
| `dev.tsv`   | 1000 |11254 |

The test data will be 

### Sample

```
Ti mɛ̀ ɓɔ̀t yɛ̂m.	Ti me bot yem.
Mı̀maŋ mi ɓodàa mi ŋâŋnā ni jɔ̀mɔ̂l.	Mimañ mi bôdaa mi ñañna ni jomol.
Mɛ̀ galɔ̀ ga hâ, ni tɛhɛ.	Me galo ga ha, ni tehe.
À m̂ɓehha mɛ kwādɛ.	A mbéhha me kwade.
Mɛ̀ ŋ́wàbal kɔɔ i ɛ̄.	Me ñwabal koo i e.
À ǹlɛm halà.	A nlem hala.
Ŋɛm u mɓoo mɛ màcèl.	Ñem u mbôô me matjél.
Kop ı̀ ŋ̀kɛk ɓɔn.	Kôp i ñkek bon.
```

## Baseline

## Evaluation

Systems will be evaluated by Word Error Rate (WER) and Character Error Rate (CER). You can run the evaluation
using the script `evaluate.py`:

```bash
$ python3 evaluate.py data/test.tsv output.tsv 
CER: 4.456824512534819
WER: 18.916666666666664
```
