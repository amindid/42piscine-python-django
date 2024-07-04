class HotBeverage:
	def __init__(self, name: str = "hot beverage", price: float = 0.30, Discription: str = "Just some hot water in a cup.") -> None:
		self.name = name
		self.price = price
		self.Description = Discription
	
	def description(self) -> str:
		return self.Description
	
	def __str__(self) -> str:
		return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"

class Coffee(HotBeverage):
	def __init__(self, name: str = "coffee", price: float = 0.40, Discription: str = "A coffee, to stay awake.") -> None:
		super().__init__(name, price, Discription)

class Tea(HotBeverage):
	def __init__(self, name: str = "tea") -> None:
		super().__init__(name)

class Chocolate(HotBeverage):
	def __init__(self, name: str = "chocolate", price: float = 0.50, Discription: str = "Chocolate, sweet chocolate..") -> None:
		super().__init__(name, price, Discription)

class Cappuccino(HotBeverage):
	def __init__(self, name: str = "cappuccino", price: float = 0.45, Discription: str = "Un po’ di Italia nella sua tazza!") -> None:
		super().__init__(name, price, Discription)
