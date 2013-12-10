#!/usr/bin/env python3

import sys
import csv
import glob

dn = sys.argv[1]

cw = csv.writer(open(dn + '.csv', "w"))
cw.writerow(['Наименование НКО', 'Учетный номер', 'ОРГН', 'Форма', 'Вид отчета', 'Период', 'URL'])

pages = glob.glob(dn + '/*.txt')

def chunks(l):
	chunks = []
	chunk = []
	for i in l:
		if i == '--- separator ---\n':
			if not chunk[0]:
				break
			while len(chunk) > 7:
				chunk[1] = chunk[1] + chunk[2]
				chunk.pop(2)	
			assert len(chunk) == 7
			chunks.append(chunk)
			chunk = []
		else:
			ii = i.replace('\xa0', ' ')
			chunk.append(ii.rstrip('\n '))
	return chunks

for p in sorted(pages):
	with open(p) as pf:
		for pl in chunks(pf.readlines()):
			if pl[0]:
				id = int(pl.pop(0))
				pl.append("http://unro.minjust.ru/NKOReports.aspx?mode=show_pdf_report&id=%u" % id)
				cw.writerow(pl)

