from elements import *

class Page():
	class InvalidArgument(Exception):
		def __init__(self,message="invalid arguent in page constructor") -> None:
			self.message = message
			super().__init__(self.message)
	def __init__(self,element) -> None:
		if not isinstance(element, Elem):
			raise self.InvalidArgument
		self.element = element
		self.only_text = [Title, H1, H2, Li, Th, Td, P, Span]
		self.alloweds = [H1, H2, Div, Table, Ul, Ol, Span, Text]

	def contain_only_text(self, elem: Elem):
		if isinstance(elem, P):
			return len(elem.content) != 0 and all(isinstance(item, Text) for item in elem.content)
		elif isinstance(elem , Span):
			if all(isinstance(item, P) for item in elem.content) and all(self.contain_only_text(item) for item in elem.content):
				return True
		if len(elem.content) == 1 and isinstance((elem.content)[0], Text):
			return True
		return False

	def recursion_check(self,elements) -> bool:
		for elem in elements.content:
			if isinstance(elem, (Ul, Ol)):
				if len(elem.content) == 0 or not all(isinstance(item, Li) for item in elem.content):
					return False
			if type(elem) in self.only_text:
				if not self.contain_only_text(elem):
					return False
			elif type(elem) != Text and len(elem.content) > 1 or isinstance(elem, Head):
				if not self.recursion_check(elem):
					return False
		return True
	
	def check_elements(self, element):
		for elem in element.content:
			if isinstance(elem, Div):
				if not self.check_elements(elem) or len(elem.content) == 0:
					return False
				continue
			for allowed in self.alloweds:
				if isinstance(elem, allowed):
					break
			else:
				return False
		return True

	def head_check(self, element):
		print(len(element.content))
		if len(element.content) == 1 and isinstance(element.content[0], Title):
			return True
		return False

	def html_check(self, element) -> bool:
		if isinstance(element,Html):
			startWithHead = False
			for elem in element.content:
				if startWithHead == False and isinstance(elem,Head):
					if not self.head_check(elem):
						return False
					startWithHead = True
				elif startWithHead == True and isinstance(elem, Body):
					if len(elem.content) == 0 or not self.check_elements(elem):
						return False
					return True
				else:
					return False
		return False

	def is_valide(self) -> bool:
		if not self.recursion_check(self.element):
			return False
		if not self.html_check(self.element):
			return False
		return True

def test():
	try:
		page = Page(Html([Head([Title(Text('eceew'))]),Body(Text('wjcbw'))]))
	except Exception as e:
		print(e)
		exit(1)
	print(page.is_valide())

if __name__ == '__main__':
	test()