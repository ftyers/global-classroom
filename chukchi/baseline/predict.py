import sys, pickle

model_file = sys.argv[1]
mf = open(model_file, 'rb')

(unigrams, bigrams) = pickle.load(mf)

unigrams['#'] = 0.0

hits = 0
n_tokens = 0
for line in sys.stdin.readlines():
	row = line.strip().split('\t')
	tokens = row[0].split(' ')
	tst_tokens = ['#'] + tokens
	n_tokens += len(tokens)
	
	output = []
	for i in range(len(tst_tokens)-1):
		up = 0.0
		bp = 0.0
		first = tst_tokens[i]
		second = tst_tokens[i+1]
		if first in bigrams:
			pred = max(bigrams[first], key=bigrams[first].get) 
			if pred == second:
				output.append(pred)
				hits += 1
#				print('!', first, '→', pred,'|||', bigrams[first][pred], file=sys.stderr)
			else:
				output += [c for c in second]
		else:
			pred = max(unigrams, key=unigrams.get) 
			if pred == second:
				output.append(pred)
				hits += 1
#				print('!', first, '→', pred,'|||', unigrams[pred], file=sys.stderr)
			else:
				output += [c for c in second]
		output.append('_')

	print('%s\t%s' % (row[0], ' '.join(output)))

print('Hits:', hits, '; Tokens:', n_tokens, file=sys.stderr)
