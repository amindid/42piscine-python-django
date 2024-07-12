import requests
from bs4 import BeautifulSoup
from sys import argv

roads = []

def search_for_url(query):
	search_url = f"https://en.wikipedia.org/{query}"
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
		return a_tags[0]['href']
	
def roads_to_philo(query):
	current_query = query
	try:
		while True:
			if current_query == "/wiki/Philosophy":
				roads.append("Philosophy")
				break
			if current_query is None:
				raise ValueError("It leads to a dead end !")
			current_query = search_for_url(current_query)
		for road in roads:
			print(road)
		print(f"{len(roads)} roads from {roads[0]} to philosophy")
	except Exception as e:
		for road in roads:
			print(road)
		print(e)


if __name__ == '__main__':
	if len(argv) != 2:
		print("invalid arguments")
		exit(1)
	roads_to_philo('wiki/' + argv[1])