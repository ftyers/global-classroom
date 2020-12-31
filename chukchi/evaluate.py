import sys 

ref_file = open(sys.argv[1])
tst_file = open(sys.argv[2])

ref_line = ref_file.readline().strip()
tst_line = tst_file.readline().strip()

bas_total = 0
ref_total = 0
tst_total = 0

# Read the ref and test files line by line
while ref_line and tst_line:
#	print(ref_line, '|||', tst_line)	

	ref_row = ref_line.split('\t')
	tst_row = tst_line.split('\t')

	if ref_row[0] != tst_row[0]:
		print('ERROR: Ref and test files are misaligned:', file=sys.stderr)
		print(ref_row, file=sys.stderr)
		print(tst_row, file=sys.stderr)

	ref_chars = ref_row[0].replace('_', '').replace(' ', '')
	tst_chars = tst_row[1].replace('_', '').replace(' ', '')
	if ref_chars != tst_chars:
		print('ERROR: Test output does not match ref output:', file=sys.stderr)
		o = ''
		for (i, j) in zip(ref_chars, tst_chars):
			if i != j:
				break
			o += i
		print(o, file=sys.stderr)
			
	bas_tokens = [c for c in ref_row[0].replace(' ', '_')]
	ref_tokens = ref_row[0].replace(' ', ' _ ').split(' ') + ['_']
	tst_tokens = tst_row[1].split(' ')

#	print('--', file=sys.stderr)
#	print('nopred:', bas_tokens, '||| oracle:', ref_tokens, '||| pred:', tst_tokens, file=sys.stderr)

	bas_clicks = len(bas_tokens)
	ref_clicks = len(ref_tokens)
	tst_clicks = len(tst_tokens)
#	print('nopred:', bas_clicks, '||| oracle:', ref_clicks, '||| pred:', tst_clicks, file=sys.stderr)

	bas_total += bas_clicks
	ref_total += ref_clicks
	tst_total += tst_clicks
#	print('clicks:', tst_clicks, '||| reduction:', tst_clicks/bas_clicks, '||| distance:', tst_clicks/ref_clicks, file=sys.stderr)

	ref_line = ref_file.readline().strip()
	tst_line = tst_file.readline().strip()

print('Characters:', bas_total)
print('Tokens:', ref_total)
print('Clicks:', tst_total)
print('Clicks/Token:', tst_total/ref_total)
print('Clicks/Character:', tst_total/bas_total)

