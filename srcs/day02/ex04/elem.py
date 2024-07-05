#!/usr/bin/python3


class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        replacements = {
            '<' : '&lt;',
            '>' : '&gt;',
            '"' : '&quot;',
            '\n': '\n<br />\n'
        }
        result = super().__str__()
        for old,new in replacements.items():
            result = result.replace(old, new)
        return result


class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """
    class ValidationError(Exception):
        def __init__(self, message="validation Error") -> None:
            self.message = message
            super().__init__(self.message)

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """
        __init__() method.

        Obviously.
        """
        # [...]
        if not (self.check_type(content) or content is None) or tag_type not in ['double', 'simple']:
            raise self.ValidationError
        self.tag = tag
        self.attr = attr
        self.content = []
        if content:
            self.add_content(content)
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        if self.tag_type == 'double':
            result = f"<{self.tag}{self.__make_attr()}>{self.__make_content()}</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{self.__make_attr()}/>"
            # [...]
        return result

    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            result += str(elem) + '\n'
        result = "  ".join(line for line in result.splitlines(True))
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    try:
        elem = Elem(tag='html', attr={}, content=[Elem(tag='head', attr={}, content=Elem(tag='title', attr={}, content=Text("Hello ground!"),tag_type='double'), tag_type='double'),Elem(tag='body',attr={},content=[Elem(tag='h1',attr={},content=Text("Oh no, not again!"), tag_type='double'),Elem(tag='img',attr={'src':'"http://i.imgur.com/pfp3T.jpg'},content=None,tag_type='simple')],tag_type='double')], tag_type='double')
        print(elem.__str__())
    except Exception as e:
        print(e)
