import sys, pickle

training_file = sys.argv[1]
model_file = sys.argv[2]

corpus = []

unigram_counts = {}
unigrams = {}
bigram_counts = {}
bigrams = {}

for line in open(training_file).readlines():
	row = line.strip().split('\t')
	tokens = row[0].split(' ')
	corpus.append(['#'] + tokens + ['#'])		

# Collect unigram counts
n_tokens = 0
for sent in corpus:
	for token in sent:
		if token not in unigram_counts:
			unigram_counts[token] = 0
		unigram_counts[token] += 1
	n_tokens += 1

# Estimate unigram probabilities
for token in unigram_counts:
	unigrams[token] = unigram_counts[token]/n_tokens

# Collect bigram counts
for sent in corpus:
	for i in range(0, len(sent)-1):
		w1 = sent[i]
		w2 = sent[i+1]
		if w1 not in bigram_counts:
			bigram_counts[w1] = {}
		if w2 not in bigram_counts[w1]:
			bigram_counts[w1][w2] = 0
		bigram_counts[w1][w2] += 1

n_bigrams = 0

# Estimate bigram probabilities
for token1 in bigram_counts:
	if token1 not in bigrams:
		bigrams[token1] = {}
	token_total = sum(bigram_counts[token1].values())
	for token2 in bigram_counts[token1]:
		if token2 not in bigrams[token1]:
			bigrams[token1][token2] = 0		
			n_bigrams += 1
		bigrams[token1][token2] = bigram_counts[token1][token2]/token_total

# Write out model
mf = open(model_file, 'wb')
pickle.dump((unigrams, bigrams), mf)
print('Written %d unigrams and %d bigrams to %s.' % (len(unigrams.keys()), n_bigrams, model_file))
