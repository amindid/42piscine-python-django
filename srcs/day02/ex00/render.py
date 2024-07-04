import sys, os, re

def render():
	if len(sys.argv) != 2:
		print("arg error !!")
		sys.exit(1)
	try:
		HTML = ""
		pairs = {}
		with open(sys.argv[1], "r") as template:
			HTML = template.read()
		with open("./settings.py", "r") as settings:
			for line in settings:
				tmp = line.split("=")
				pairs[tmp[0].strip()] = tmp[1].strip().replace('"', '')
		with open("./result.html", "w") as result:
			result.write(HTML.format(**pairs))
	except Exception as e:
		print(f"exception accured : {e}")
		sys.exit(1)


if __name__ == '__main__':
	render()