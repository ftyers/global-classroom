all: model.tsv output.tsv
	python3 ../evaluate.py ../data/dev.tsv output.tsv

model.tsv:
	python3 train.py ../data/train.tsv model.tsv

output.tsv:
	python3 convert.py model.tsv < ../data/dev.tsv > output.tsv

clean:
	rm output.tsv model.tsv
