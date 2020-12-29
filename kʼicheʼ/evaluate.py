import sys, copy

def evaluate(ref, hyp):
	"""
		Takes two strings, a reference and an output from the system, e.g.
		  ref = ch>aw>e
		  hyp = ch>awe
		and produces the precision, recall and F-score, e.g.
		  P = 1/3 = 0.333
		  R = 1/2 = 0.5
		  F = 2.0 / ((1.0/0.333)+(1/0.5)) = 0.3997
	"""
	ref = ref.split('>')
	sys = hyp.split('>')
	res = copy.copy(sys)
	
	# Find out how many matches we got, this way we can check for matches
	# that are duplicated
	matched = 0
	for r in ref:
		if r in res:
			matched += 1
			res.remove(r)
	
	# If we got 0 matches then we can't calculate a score, return 0s
	if matched == 0:
		return (0.0, 0.0, 0.0)
	
	# Calculate precision and recall
	P = matched/len(ref)
	R = matched/len(sys)

	# Calculate F-score
	F = 2.0 / ((1.0/P)+(1.0/R))

	return (P, R, F)

n_tokens = 0
n_sents = 0

if len(sys.argv) != 3:
	print('evaluate.py <ref file> <test file>')
	sys.exit(-1)

ref_file = open(sys.argv[1])
tst_file = open(sys.argv[2])

ref_line = ref_file.readline().strip()
tst_line = tst_file.readline().strip()

Ps = []
Rs = []
Fs = []

# Read the ref and test files line by line
while ref_line and tst_line:
#	print(ref_line, '|||', tst_line)	

	ref_row = ref_line.split('\t')
	tst_row = tst_line.split('\t')

	if ref_row[0] != tst_row[0]:
		print('ERROR: Ref and test files are misaligned:', file=sys.stderr)
		print(ref_row)
		print(tst_row)

	ref = ref_row[1].split(' ')
	hyp = tst_row[1].split(' ')

	# Collect the individual precision and recalls
	for (r, h) in zip(ref, hyp):
		(p, r, f) = evaluate(r, h)
		Ps.append(p)
		Rs.append(r)
		Fs.append(f)

	# Update the number of tokens and sentences
	n_tokens += len(ref)	
	n_sents += 1

	ref_line = ref_file.readline().strip()
	tst_line = tst_file.readline().strip()

print('%d sentences read, %d tokens' % (n_sents, n_tokens))
# Average the precision and recall over the number of tokens
print('P:', sum(Ps)/n_tokens)
print('R:', sum(Rs)/n_tokens)
print('F:', sum(Fs)/n_tokens)
