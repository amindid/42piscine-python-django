import requests, json, dewiki, sys


def main():
	if len(sys.argv) != 2:
		print("invalid arguments")
		exit(1)
	wiki_endPoint = "https://en.wikipedia.org/w/api.php"
	params = {
		'action'      : 'query',
		'format'      : 'json',
		'titles'      : sys.argv[1],
		'prop'        : 'extracts',
		'explaintext' : False
	}
	response = requests.get(wiki_endPoint, params=params)
	if response.status_code == 200:
		data = response.json()
		pages = data['query']['pages']
		for page_id, page in pages.items():
			try:
				name = page['title'] + '.wiki'
				value = page['extract']
				with open(name, 'w') as file:
					file.write(value)
			except Exception as e:
				print("Information not found")
	else:
		print(f"ERROR: {response.status_code} {response.reason}")


if __name__ == '__main__':
	main()