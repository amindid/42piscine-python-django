from elements import *

class Page():
	def __init__(self,element) -> None:
		self.element = element

	def recursion_check(self,elements) -> bool:
		for elem in elements:
			if isinstance(elem, list):
				if not self.recursion_check(elem):
					return False
			elif not isinstance(elem, Elem):
				return False
		return True
	
	def html_check(self, element) -> bool:
		if isinstance(element, list) and isinstance(element[0],Html):
			for elem in element[0]:
				if isinstance(elem, list) and isinstance(elem[0],Head) and isinstance(elem[1],Body):
					return True
				break
			# if isinstance(html.content[0],Head) and isinstance(html.content[1], Body):
				# return True

		return False 

	def is_valide(self) -> bool:
		# if not self.recursion_check(self.element):
		# 	return False
		if not self.html_check(self.element):
			return False
		return True

def test():
	page = Page([Html([Head(),Body()])])
	print(page.is_valide())

if __name__ == '__main__':
	test()