import sys 

t = open(sys.argv[1]).readlines()

dico = {}

for line in t:
	row = line.strip().split('\t')
	for (aglcw, mpw) in zip(row[0].split(' '), row[1].split(' ')):	
		if mpw not in dico:
			dico[mpw] = {}
		if aglcw not in dico[mpw]:
			dico[mpw][aglcw] = 0
		dico[mpw][aglcw] += 1

outf = open(sys.argv[2], 'w+')

vcs = 0
for mpw in dico:
	total = sum(dico[mpw].values())
	for aglcw in dico[mpw]:
		print('%.4f\t%s\t%s' % (dico[mpw][aglcw] / total, mpw, aglcw), file=outf)
	vcs += 1

print('Stored %d words' % (vcs))
outf.close()
