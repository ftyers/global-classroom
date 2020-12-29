import sys

dico = {}

table = {}

for line in open(sys.argv[1]).readlines():
	# P in out
	(p, mpw, aglcw) = line.strip().split('\t')
	if mpw not in dico:
		dico[mpw] = {}
	if aglcw not in dico[mpw]:
		dico[mpw][aglcw] = 0.0
	dico[mpw][aglcw] = float(p)
		
for mpw in dico:
	wmax = 0.0
	for aglcw in dico[mpw]:
		if dico[mpw][aglcw] > wmax:
			table[mpw] = aglcw

for line in sys.stdin.readlines():
	row = line.strip().split('\t')
	
	outs = ''
	first = True
	for mpw in row[0].split(' '):
		sep = ' '
		if first:
			sep = ''
			first = False
		if mpw in table:
			outs = outs + sep + table[mpw]
		else:
			outs = outs + sep + mpw
	print('%s\t%s' % (row[0], outs))	
