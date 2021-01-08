all: model.att output.tsv
	python3 ../evaluate.py ../data/dev.tsv output.tsv

model.att:
	python3 train.py ../data/train.tsv model.att

output.tsv:
	cat ../data/dev.tsv | python3 segment.py model.att > output.tsv

clean:
	rm output.tsv model.att
