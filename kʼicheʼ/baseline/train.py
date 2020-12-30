import sys

eps = '@0@'

t = open(sys.argv[1]).readlines()
mf = open(sys.argv[2], 'w+')

morphs = {}

for line in t:
	row = line.strip().split('\t')
	
	for token in row[1].split(' '):
		token = token.strip('')
		for morph in token.split('>'):
			if morph not in morphs:
				morphs[morph] = 0
			morphs[morph] += 1

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
