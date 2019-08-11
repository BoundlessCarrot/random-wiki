#random wikipedia thing; 
#url = https://en.wikipedia.org/wiki/Special:Random
#test url: https://www.google.com/
#test url 2: https://en.wikipedia.org/wiki/Stack_Overflow

import wikipedia as wiki
#import requests
#from bs4 import BeautifulSoup as bs

#def opener():
#	wikiPage = requests.get('https://en.wikipedia.org/wiki/Special:Random')
#	
#	try:
#		assert (wikiPage.status_code == 200)
#	except AssertionError:
#		return "Link is not accessible"
#	
#	raw = wikiPage.content
#	wikiSoup = bs(raw, 'lxml')
#	
#	pageData = wikiSoup.title.string
#	return pageData
		
def printer():
#	pagedata = opener()
#	page = wiki.page(pagedata)
	l = wiki.random(pages=1)
	page = wiki.page(l)
#	print(pagedata, page, page1)
	try:
		print(page.title)
		print(page.url)
		print()
		print(wiki.summary(l))
	except wikipedia.exceptions.PageError:
		print("Something went wrong. Please try again!")
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

def decision(page): #purely for navigating in the terminal, should have no use wthin a UI
	inp = input("\n'next' for a new page, 'links' for links on this page, 'pics' for pictures on this page, 'q' to exit: ")
	if 'next' in inp.casefold():
		print()
		printer()
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