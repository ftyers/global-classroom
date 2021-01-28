import sys, pickle

# This is the training data
training_file = sys.argv[1]
# This is the filename that we will save the model in
model_file = sys.argv[2]

# This is a list of sentences in the training data
corpus = []

# Unigram counts = how often we see tokens, e.g. a frequency list
unigram_counts = {}
# Probability of the individual unigram
unigrams = {}
# How often we see word2 after word1 (e.g. 'house' after 'big')
bigram_counts = {} # bigram_counts['big']['house'] = 1, bigram_counts['big']['dog'] = 1
# Probability of word2 after word1
bigrams = {} # bigrams['big']['house'] 0.5, ...

# Read in the examples from the training data
for line in open(training_file).readlines():
	# Each line in the training data is two columns
	# тыкгаткэта ивнин риӄукэтэ	ты>кгат>кэ>та ив>ни>н риӄукэ>тэ
	row = line.strip().split('\t')
	# The tokens are in the first column
	tokens = row[0].split(' ')
	# Add the tokens to the list of sentences, with a beginning of sentence and an end of sentence marker
	corpus.append(['#'] + tokens + ['#'])		

# Collect unigram counts
n_tokens = 0 # Number of tokens
# For each of the sentences in our corpus
for sent in corpus:
	# For each of the tokens in the sentence
	for token in sent:
		# If we haven't seen the token before:
		if token not in unigram_counts:
			# Initialise the token count to zero
			unigram_counts[token] = 0
		# Increment the count of that token
		unigram_counts[token] += 1
	# Increment the count of all the tokens
	n_tokens += 1

# Estimate unigram probabilities
# For each of the types we have seen 
for token in unigram_counts:
	# The probability is the frequency of the token divided by the total number of tokens
	unigrams[token] = unigram_counts[token]/n_tokens

# Collect bigram counts
# e.g. ['the', 'big', 'house'] 
# bigrams: (the, big) (big, house)
# For each of the sentences in the corpus
for sent in corpus:
	# For each number in the range of 0..length of sentence - 1
	for i in range(0, len(sent)-1):
		# The first word is the word at i
		w1 = sent[i]
		# The second word is the word at i+1
		w2 = sent[i+1]
		# If we haven't seen the first word before, initialise a new dictionary for the second word
		if w1 not in bigram_counts:
			bigram_counts[w1] = {}
		# If we haven't seen the second word before, initialise the count to 0
		if w2 not in bigram_counts[w1]:
			bigram_counts[w1][w2] = 0
		# Increment the count
		bigram_counts[w1][w2] += 1

n_bigrams = 0

# Estimate bigram probabilities
# For each of the first words
for token1 in bigram_counts:
	# If we haven't seen it before, initialise it
	if token1 not in bigrams:
		bigrams[token1] = {}
	# Find the total frequency of all of the words that can go after this word
	token_total = sum(bigram_counts[token1].values())
	# For each of the second parts of the bigram
	for token2 in bigram_counts[token1]:
		# If we haven't seen the  second part before, initialise it to 0
		if token2 not in bigrams[token1]:
			bigrams[token1][token2] = 0		
			n_bigrams += 1
		# Calculate the probability
		bigrams[token1][token2] = bigram_counts[token1][token2]/token_total

# Write out model
mf = open(model_file, 'wb')
pickle.dump((unigrams, bigrams), mf)
print('Written %d unigrams and %d bigrams to %s.' % (len(unigrams.keys()), n_bigrams, model_file))
