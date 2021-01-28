import sys 
from ATT import ATTFST # Library for processing transducers

# Load the model using the library
a = ATTFST(sys.argv[1])

# For each of the lines in the input
# e.g. Ri numam xkamik are taq kʼo jumuchʼ lajuj ujunabʼ .	Ri nu>mam x>kamik are taq kʼo jumuchʼ lajuj u>junabʼ .
for line in sys.stdin.readlines():
	# We split it into two
	row = line.strip().split('\t')

	output = [] # List of output tokens
	# For each of the tokens in the first column, splitting on space
	for token in row[0].split(' '):
		# Apply the model we created to the token, and get the possible segmentations back
		segs = a.apply(token)
		# This pulls out the first item in the list of results
		max_seg = ''
		for seg in segs:
			max_seg = seg
			break
		# If there is an actual result, i.e. the model found a segmentation
		if max_seg:
			# We append it to the output
			output.append(max_seg[0].strip('>'))
		else:
			# Otherwise we just append the token itself without segmentation
			output.append(token)
			
	# Print out the input row and the output row, joining the output row on space
	print('%s\t%s' % (row[0], ' '.join(output)))	
