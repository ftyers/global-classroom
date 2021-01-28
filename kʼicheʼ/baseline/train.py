import sys

eps = '@0@'

t = open(sys.argv[1]).readlines()
mf = open(sys.argv[2], 'w+')

# Dictionary of morph → frequency
morphs = {}

# Ri numam xkamik are taq kʼo jumuchʼ lajuj ujunabʼ .	Ri nu>mam x>kamik are taq kʼo jumuchʼ lajuj u>junabʼ .
for line in t:
	# Split line in to columns
	row = line.strip().split('\t')
	
	# For each of the tokens in the second column, e.g. [Ri, nu>mam, ...]
	for token in row[1].split(' '):
		token = token.strip('')
		# For each of the morphs in the token, e.g. [nu, mam]
		for morph in token.split('>'):
			# If we haven't seen the morph before add to our list
			if morph not in morphs:
				morphs[morph] = 0
			# Increment its count
			morphs[morph] += 1

# Here we define a finite-state transducer
initial_state = 0
current_state = 0
for morph in morphs:
	state = initial_state
	for i in range(len(morph)):
		c = morph[i]
		print('%d\t%d\t%s\t%s\t%.4f' % (state, current_state+1, c, c, 0.0), file=mf)
		current_state += 1
		state = current_state
	print('%d\t%d\t%s\t%s\t%.4f' % (current_state, 0, eps, '>', 1.0/morphs[morph]), file=mf)

print('%d\t%.4f' % (0, 0.0), file=mf)

print('%d morphemes written' % len(morphs.keys()), file=sys.stderr)
