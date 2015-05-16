#!/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import yaml
import json

def md2dict(text):
	config, content = text.split('\n---')
	data = dict()
	data['config'] = yaml.load(config)	
	data['content'] = content
	return data

def md2json(text):
	data = md2dict(text)
	return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
	if len(sys.argv) == 2:
		filepath = sys.argv[1]
		with open(filepath, 'r') as f:
			text = f.read()
			print md2json(text)
