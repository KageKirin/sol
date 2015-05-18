#!/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import yaml
import json

def md2dict(text):
	"""
	splits then text into YAML front matter config and markdown content
	"""
	config, content = text.split('\n---')
	data = dict()
	data['config'] = yaml.load(config)
	data['content'] = content
	return data

def multimd2dict(text):
	"""
	splits then text into YAML front matter config and several markdown content parts
	"""
	parts = text.split('\n---')
	data = dict()
	data['config'] = yaml.load(parts[0])
	data['content'] = parts[1:]
	return data

def md2json(text):
	data = md2dict(text)
	return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

def multimd2json(text):
	data = multimd2dict(text)
	return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
	if len(sys.argv) == 2:
		filepath = sys.argv[1]
		with open(filepath, 'r') as f:
			text = f.read()
			print md2json(text)
