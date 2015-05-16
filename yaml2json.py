#!/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import yaml
import json

def yaml2yaml(text):
	data = yaml.load(text)
	return yaml.dump(data, default_flow_style=False, indent=4, allow_unicode=True)

def yaml2json(text):
	data = yaml.load(text)
	return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
	if len(sys.argv) == 2:
		filepath = sys.argv[1]
		with open(filepath, 'r') as f:
			text = f.read()
			print yaml2json(text)
