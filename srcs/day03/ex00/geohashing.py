import sys

def main():
	if len(sys.argv) != 5:
		print("invalid args : correct args should be : date dow x_location y_location")
		exit(1)
	date = sys.argv[1]
	dow = sys.argv[2]
	x_location = sys.argv[3]
	y_location = sys.argv[4]

if __name__ == '__main__':
	main()