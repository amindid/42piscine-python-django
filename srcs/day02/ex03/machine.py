import random
from beverages import *

class CoffeeMachine:
	def __init__(self) -> None:
		self.broken = False
		self.served = 0

	class EmptyCup(HotBeverage):
		def __init__(self, name: str = "empty cup", price: float = 0.90, Discription: str = "An empty cup?! Gimme my money back") -> None:
			super().__init__(name, price, Discription)
	
	class BrokenMachineException(Exception):
		def __init__(self, message="This coffee machine has to be repaired") -> None:
			self.message = message
			super().__init__(self.message)
	
	def repair(self) -> None:
		if self.broken:
			self.broken = False
			self.served = 0
	
	def serve(self, drink: HotBeverage) -> HotBeverage:
		if self.served == 10:
			self.broken = True
			raise self.BrokenMachineException
		self.served += 1
		if random.choice([True, False]):
			return drink
		else:
			return self.EmptyCup()

def main():
	machine = CoffeeMachine()
	drink = HotBeverage()
	drink = machine.serve(Coffee())
	print(drink.__str__())
	drink = machine.serve(Tea())
	print(drink.__str__())
	drink = machine.serve(Chocolate())
	print(drink.__str__())
	drink = machine.serve(Cappuccino())
	print(drink.__str__())
	drink = machine.serve(HotBeverage())
	print(drink.__str__())
	drink = machine.serve(Coffee())
	print(drink.__str__())
	drink = machine.serve(Tea())
	print(drink.__str__())
	drink = machine.serve(Chocolate())
	print(drink.__str__())
	drink = machine.serve(Cappuccino())
	print(drink.__str__())
	drink = machine.serve(HotBeverage())
	print(drink.__str__())
	try:
		drink = machine.serve(HotBeverage())
		print(drink.__str__())
	except machine.BrokenMachineException as e:
		print(e)
	machine.repair()
	drink = machine.serve(Coffee())
	print(drink.__str__())
	drink = machine.serve(Tea())
	print(drink.__str__())
	drink = machine.serve(Chocolate())
	print(drink.__str__())
	drink = machine.serve(Cappuccino())
	print(drink.__str__())
	drink = machine.serve(HotBeverage())
	print(drink.__str__())
	drink = machine.serve(Coffee())
	print(drink.__str__())
	drink = machine.serve(Tea())
	print(drink.__str__())
	drink = machine.serve(Chocolate())
	print(drink.__str__())
	drink = machine.serve(Cappuccino())
	print(drink.__str__())
	drink = machine.serve(HotBeverage())
	print(drink.__str__())
	try:
		drink = machine.serve(HotBeverage())
		print(drink.__str__())
	except machine.BrokenMachineException as e:
		print(e)
	


if __name__ == '__main__':
	main()