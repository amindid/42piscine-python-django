import requests
from bs4 import BeautifulSoup
from sys import argv

roads = []
def find_philosophy(query):
	pass

def search_for_url(query):
	search_url = f"https://en.wikipedia.org/{query}"
	print(search_url)
	response = requests.get(search_url).content
	result = BeautifulSoup(response, 'html.parser')
	title = result.find(id='firstHeading').find('span').contents[0]
	if title in roads:
		raise ValueError("It leads to an infinite loop !")
	roads.append(title)
	p_tags = result.find(id='mw-content-text').find_all('p')
	a_tags = []
	for p in p_tags:
		if len(a_tags := p.find_all('a')) != 0:
			break
	else:
		raise ValueError("It leads to a dead end !")
	if a_tags[0].get('href') is not None and a_tags[0]['href'].startswith('/wiki/') and not a_tags[0]['href'].startswith('/wiki/Wikipedia:') and not a_tags[0]['href'].startswith('/wiki/Help:'):
		print(f"----- {a_tags[0]['href']}")
		return a_tags[0]['href']
	
def roads_to_philo(query):
	current_query = query
	roads.append(query)
	count = 1
	try:
		while True:
			print(current_query)
			current_query = search_for_url(current_query)
			if current_query in roads:
				raise ValueError("It leads to an infinite loop !")
			# roads.append(current_query)
			count += 1
			if current_query == "Philosophy":
				break
		for road in roads:
			print(road)
		print(f"{count} roads from {query} to philosophy")
	except Exception as e:
		print(e)


if __name__ == '__main__':
	if len(argv) != 2:
		print("invalid arguments")
		exit(1)
	roads_to_philo('wiki/' + argv[1])