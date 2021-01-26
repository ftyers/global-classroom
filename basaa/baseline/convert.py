import sys

dico = {}

table = {}

# This code loads the model from the file
for line in open(sys.argv[1]).readlines():
	# P in out
	(p, mpw, aglcw) = line.strip().split('\t')
	if mpw not in dico:
		dico[mpw] = {}
	if aglcw not in dico[mpw]:
		dico[mpw][aglcw] = 0.0
	dico[mpw][aglcw] = float(p)
		
# Find the maximum probability for each missionary token
for mpw in dico:
	wmax = 0.0
	# For each of the general tokens for this missionary token
	for aglcw in dico[mpw]:
		# If the probability is higher than wmax
		if dico[mpw][aglcw] > wmax:
			# Set this token as the most probable
			table[mpw] = aglcw
			# Update the wmax 
			wmax = dico[mpw][aglcw] 

# For each of the lines in the input
for line in sys.stdin.readlines():
	# Split the line into columns
	row = line.strip().split('\t')
	
	outs = ''
	first = True
	# For each of the tokens in the line
	for mpw in row[0].split(' '):
		sep = ' '
		if first:
			sep = ''
			first = False
		# If we have seen the token before and know its maximum probability conversion
		if mpw in table:
			outs = outs + sep + table[mpw]
		# Or if we haven't the token, we just output itself
		else:
			outs = outs + sep + mpw
	# Print the line
	print('%s\t%s' % (row[0], outs))	
