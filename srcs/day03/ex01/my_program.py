from path import Path

def main():
	try:
		Path.makedirs("./new_dir")
	except Exception as e:
		print(f"Exception : {e}")
	try:
		with open("./new_dir/new_file.txt", "w") as file:
			file.write('somthing')
		with open("./new_dir/new_file.txt", "r") as file:
			input = file.read()
			print(f"file content : {input}")
	except Exception as e:
		print(f"Exception : {e}")

if __name__ == '__main__':
	main()