#random wikipedia thing; 
#url = https://en.wikipedia.org/wiki/Special:Random
#test url: https://www.google.com/
#test url 2: https://en.wikipedia.org/wiki/Stack_Overflow

import wikipedia as wiki

wikiHistory = []

def printer(page=None):
	if page == None:
		l = wiki.random(pages=1)
		page = wiki.page(l)

		try:
			print(page.title)
			print(page.url)
			print()
			print(wiki.summary(l))
		except wikipedia.exceptions.DisambiguationError as e:
			print(e.options)
	else:
		try:
			print(page.title)
			print(page.url)
			print()
			print(wiki.summary(page))
		except wikipedia.exceptions.DisambiguationError as e:
			print(e.options)
	
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
	global wikiHistory
	wikiHistory.append(page)
	inp = input("\ntype 'next' for a new page, 'prev' for the previous page, 'full' to show the full page, 'links' for links on this page, 'pics' for pictures on this page, 'history' to show your complete history, 'q' to exit: ").casefold()
	if 'next' in inp:
		print('\n--------------------------------------------------------\n')
		printer()
	elif 'prev' in inp:
		print('\n--------------------------------------------------------\n')
		printer(wikiHistory[-2])
		decision(page)
	elif 'full' in inp:
		print('\n--------------------------------------------------------\n')
		pageExpander(page)
		decision(page)
	elif 'links' in inp:
		print()
		linkCollector(page)
		decision(page)
	elif 'pics' in inp:
		print()
		picCollector(page)
		decision(page)
	elif 'history' in inp:
		print('\n--------------------------------------------------------\n')
		for item in wikiHistory:
			print(str(item.title) + ': ' + str(item.url))
		print('\n--------------------------------------------------------\n')
		decision(page)
	elif 'q' in inp:
		exit()
	else:
		print("I don't know what you're trying to say here, try again")
		decision(page)

if __name__ == '__main__':
	printer()