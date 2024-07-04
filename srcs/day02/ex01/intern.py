class intern:
	def __init__(self, name: str = "My name? I’m nobody, an intern, I have no name."):
		self.name = name

	def __str__(self) -> str:
		return self.name
	

	class coffee:
		def __init__(self) -> None:
			pass

		def __str__(self) -> str:
			return "This is the worst coffee you ever tasted."
		
	def work(self):
		raise Exception("I’m just an intern, I can’t do that...")
	
	def make_coffee(self) -> coffee:
		return self.coffee()
	
def main():
	intern1 = intern()
	intern2 = intern("Mark")
	print(f"intern1 name : {intern1.__str__()}")
	print(f"intern2 name : {intern2.__str__()}")
	coffee = intern2.make_coffee()
	print(coffee.__str__())
	try:
		intern1.work()
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()