all: model.dat output.tsv
	python3 ../evaluate.py ../data/dev.tsv output.tsv

model.dat:
	python3 train.py ../data/train.tsv model.dat

output.tsv:
	python3 predict.py model.dat < ../data/dev.tsv > output.tsv

clean:
	rm model.dat output.tsv
