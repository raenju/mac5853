import re

def busca_armamentos(site):
	s = site.html
	matches = 0
	if re.search('(?i)arma', s) is not None:
		matches = matches + 1
	if re.search('(?i)calibre', s) is not None:
		matches = matches + 1
	if re.search('(?i)muni[cç][aã]o|(?i)muni[cç][oõ]es', s) is not None:
		matches = matches + 1

	if matches >= 2:
		return True
	return False

def classificate(site):
	reasons = []
	if busca_armamentos(site):
		reasons.append("Armamentos")

	return reasons