import sys 

# opens the training corpus and reads in all the lines
t = open(sys.argv[1]).readlines()

dico = {}

# for each line in the training corpus
for line in t:
	# split the two columns
	row = line.strip().split('\t')
	# [Ti, me, bot, yem.]	[Ti, mɛ̀, ɓɔ̀t, yɛ̂m.]
	# (Ti, Ti) (me, mɛ̀), (bot, ɓɔ̀t) (yem, yɛ̂m.)
	for (mpw, aglcw) in zip(row[0].split(' '), row[1].split(' ')):	
		# If the missionary token is not in the dictionary
		if mpw not in dico:
			# Make a new dictionary for that token
			# This dictionary will contain all the possible General Alphabet variants
			dico[mpw] = {}
		# If the general alphabet variant has not been seen before for this Missionary token
		if aglcw not in dico[mpw]:
			# Set its count to 0
			dico[mpw][aglcw] = 0
		# Increment the count
		dico[mpw][aglcw] += 1

# By the end of this loop, we have a dictionary where each missionary token
# is paired with all of its potential General tokens, and there is a frequency for each one

# Open a file for the model 
outf = open(sys.argv[2], 'w+')

# A counter for the vocabulary size
vcs = 0
# For each of the missionary tokens
for mpw in dico:
	# Find the total frequency of the token (e.g. sum of all the matches with a General token)
	total = sum(dico[mpw].values())
	# For each fo the general tokens
	for aglcw in dico[mpw]:
		# Print the probability of that token given the missionary token
		print('%.4f\t%s\t%s' % (dico[mpw][aglcw] / total, mpw, aglcw), file=outf)
	vcs += 1

print('Stored %d words' % (vcs))
outf.close()
