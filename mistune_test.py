#!/bin/python
import os
import os.path
import mistune

if __name__ == '__main__':
	root = os.path.dirname(__file__)
	filepath = os.path.join(
		root, 'markdown_documentation_syntax.text'
	)
	with open(filepath, 'r') as f:
		text = f.read()

	d = mistune.markdown(text)
	print d
