#!/usr/bin/python3
import sys
import antigravity

def main():
	if len(sys.argv) != 4:
		print("invalid args : correct args should be : date_dow x_location y_location")
		exit(1)

	try:
		date_dow = sys.argv[1].encode('utf-8')
	except Exception as e:
		return(print(e))
	try:
		x_location = float(sys.argv[2])
	except Exception as e:
		return(print("x_location should be float value"))
	try:
		y_location = float(sys.argv[3])
	except Exception as e:
		return(print("y_location should be float value"))
	try:
		print(antigravity.geohash(x_location, y_location, date_dow))
	except Exception as e:
		return(print(e))

if __name__ == '__main__':
	main()