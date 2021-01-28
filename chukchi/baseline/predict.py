import sys, pickle

# This is the filename of the model file
model_file = sys.argv[1]
mf = open(model_file, 'rb')

# Load the unigram and bigram probabilities from the model file
(unigrams, bigrams) = pickle.load(mf)

# Initialise the probability of the start of the sentence.
unigrams['#'] = 0.0

# Hits is number of times we get a prediction right
hits = 0
# The number of tokens
n_tokens = 0
# For each of the lines in the input
for line in sys.stdin.readlines():
	# Split into two columns
	row = line.strip().split('\t')
	# Our tokens are in column one, split by space
	tokens = row[0].split(' ')
	# The test tokens are the beginning of sentence symbol + the list of tokens
	tst_tokens = ['#'] + tokens
	# Increment the number of tokens by the length of the list containing the tokens
	n_tokens += len(tokens)
	
	# This is our output
	output = []
	# For each of the tokens in the "tst_tokens" list (e.g. the list + the beginning of sentence symbol)
	for i in range(len(tst_tokens)-1):
		up = 0.0 # Unigram probability
		bp = 0.0 # Bigram probability
		first = tst_tokens[i] # First token in bigram
		second = tst_tokens[i+1] # Second token in bigram
		# If we find the first token in the bigrams dict
		if first in bigrams:
			# We get the best prediction for what token should come next
			pred = max(bigrams[first], key=bigrams[first].get) 
			# If it matches with what the next token really is
			if pred == second:
				# We add this whole token to the output
				# e.g. a single click on a prediction
				output.append(pred)
				# Increment the number of hits by 1
				hits += 1
			else:
				# Otherwise we add each individual character to the output
				# e.g. writing out each of the individual clicks
				output += [c for c in second]
		# If we haven't found a bigram, we just try proposing the most frequent unigram
		else:
			# Find the highest scoring unigram
			pred = max(unigrams, key=unigrams.get) 
			# If the prediction is right
			if pred == second:
				# Append to output
				output.append(pred)
				hits += 1
#				print('!', first, '→', pred,'|||', unigrams[pred], file=sys.stderr)
			else:
				# Otherwise append each individual character
				output += [c for c in second]
		# Finally append a space symbol
		output.append('_')

	# Print out our input and the predicted sequence of keypresses
	print('%s\t%s' % (row[0], ' '.join(output)))

print('Hits:', hits, '; Tokens:', n_tokens, file=sys.stderr)
