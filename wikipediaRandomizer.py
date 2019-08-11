#random wikipedia thing; 
#url = https://en.wikipedia.org/wiki/Special:Random
#test url: https://www.google.com/
#test url 2: https://en.wikipedia.org/wiki/Stack_Overflow

import wikipedia as wiki

def printer():
	l = wiki.random(pages=1)
	page = wiki.page(l)
	
	print(page.title)
	print(page.url)
	print()
	print(wiki.summary(l))
	
	decision(page)

def linkCollector(page):
	rawLinks = page.links
	for x in rawLinks:
		y = x.replace(' ', '_')
		print('https://en.wikipedia.org/wiki/' + y)

def picCollector(page):
	imageLinks = page.images
	for link in imageLinks:
		print(link)

def pageExpander(page):
	print(page.title)
	print()
	print(page.content)

def decision(page): #purely for navigating in the terminal, should have no use wthin a UI
	inp = input("\n'next' for a new page, 'full' to show the full page, 'links' for links on this page, 'pics' for pictures on this page, 'q' to exit: ")
	if 'next' in inp.casefold():
		print()
		print('----------------------------')
		print()
		printer()
	elif 'full' in inp.casefold():
		print()
		print('----------------------------')
		print()
		pageExpander(page)
		decision(page)
	elif 'links' in inp.casefold():
		print()
		linkCollector(page)
		decision(page)
	elif 'pics' in inp.casefold():
		print()
		picCollector(page)
		decision(page)
	elif 'q' in inp.casefold():
		exit()
	else:
		print("I don't know what you're trying to say here, try again")
		decision(page)

if __name__ == '__main__':
	printer()