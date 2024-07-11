import requests, dewiki
from sys import argv

def main():
	if len(argv) != 2:
		print("invalid arguments")
		exit(1)
	words = [word.capitalize() for word in argv[1].split()]
	title = "_".join(words)
	wiki_endPoint = "https://en.wikipedia.org/w/api.php"
	params = {
		'action'      : 'query',
		'format'      : 'json',
		'titles'      : title,
		'prop'        : 'extracts',
		'explaintext' : False
	}
	response = requests.get(wiki_endPoint, params=params)
	if response.status_code == 200:
		data = response.json()
		pages = data['query']['pages']
		for page_id, page in pages.items():
			try:
				name = (page['title']).replace(' ', '_') + '.wiki'
				value = dewiki.from_string(page['extract'])
				with open(name, 'w') as file:
					file.write(value)
			except Exception as e:
				print("Information not found")
	else:
		print(f"ERROR: {response.status_code} {response.reason}")


if __name__ == '__main__':
	main()

