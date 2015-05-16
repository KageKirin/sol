#!/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import yaml
import json

def json2json(text):
	data = json.loads(text)
	return json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))

def json2yaml(text):
	data = json.loads(text)
	return yaml.dump(data, default_flow_style=False, indent=4, allow_unicode=True)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		filepath = sys.argv[1]
		with open(filepath, 'r') as f:
			text = f.read()
			print json2yaml(text)
