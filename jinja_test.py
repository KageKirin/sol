#!/bin/python

import jinja2

if __name__ == '__main__':
	template = jinja2.Template('Hello {{ name }}!')
	d= template.render(name='John Doe')
	print d


