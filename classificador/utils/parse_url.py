def parse(string):
	return [site for site in string.split()]

def get_domain(url):
	blocks = url.split("/")
	index = 0
	if url.startswith("http"):
		index = 1
		if not blocks[index]:
			index = index + 1
	if blocks[index].startswith("www."):
		blocks[index] = blocks[index][4:]
	return blocks[index]