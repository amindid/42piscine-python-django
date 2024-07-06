from elem import *

class Html(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'html'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Head(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'head'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Body(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'body'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Title(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'title'
		self.attr = attr
		# self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, content, self.tag_type)

class Meta(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'meta'
		self.attr = attr
		self.content = content
		self.tag_type = 'simple'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Img(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'img'
		self.attr = attr
		self.content = content
		self.tag_type = 'simple'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Table(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'table'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Th(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'th'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Tr(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'tr'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Td(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'td'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Ul(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'ul'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Ol(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'ol'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Li(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'li'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class H1(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'h1'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class H2(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'h2'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class P(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'p'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Div(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'div'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Span(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'span'
		self.attr = attr
		self.content = content
		self.tag_type = 'double'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Hr(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'hr'
		self.attr = attr
		self.content = content
		self.tag_type = 'simple'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)

class Br(Elem):
	def __init__(self,content=None,attr={}):
		self.tag = 'br'
		self.attr = attr
		self.content = content
		self.tag_type = 'simple'
		super().__init__(self.tag, self.attr, self.content, self.tag_type)