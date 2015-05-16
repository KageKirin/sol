#!/bin/python
import os
import os.path
import markdown

if __name__ == '__main__':
	root = os.path.dirname(__file__)
	filepath = os.path.join(
		root, 'markdown_documentation_syntax.text'
	)
	with open(filepath, 'r') as f:
		text = f.read()
	
	d = markdown.markdown(text, ['gfm'])
	print d
