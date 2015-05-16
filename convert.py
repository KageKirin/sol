#!/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import yaml
import json
import string
import fnmatch
import markdown
import mistune
import jinja2
from glob import glob
from md2json import md2dict, md2json

#os.getcwd()
config_pages_dir = '_pages'
config_page_ext = '.md'

config_templates_dir = '_templates'
config_template_ext = '.html'

templateLoader = jinja2.FileSystemLoader(searchpath=config_templates_dir)
templateEnv = jinja2.Environment(loader=templateLoader)


def load_from_dir(folder, extension):
	matches = []
	for root, dirnames, filenames in os.walk(folder):
		for filename in fnmatch.filter(filenames, '*'+extension):
			matches.append(os.path.join(root, filename))
	return matches

def load_pages():
	return load_from_dir(folder=config_pages_dir, extension=config_page_ext)


def load_templates():
	return load_from_dir(folder=config_templates_dir, extension=config_template_ext)


def convert_page_dict(pagedict):
	htmlPage = ""
	if pagedict["config"] and pagedict["content"]:
		config = pagedict["config"]
		htmlContent = markdown.markdown(pagedict["content"], ['gfm'])
		if config.has_key("template"):
			print config["template"]
			tpl = templateEnv.get_template(config["template"])
			if tpl:
				pagedict["htmlContent"] = htmlContent
				htmlPage = tpl.render(pagedict)
				print htmlPage
	return htmlPage


def convert_page(page):
	d = dict()
	with open(page, 'r') as f:
			text = f.read()
			d = md2dict(text)
			convert_page_dict(d)


def convert_pages(pages):
	for p in pages:
		convert_page(p)


if __name__ == '__main__':
	pages = load_pages()
	#templates = load_templates()	
	convert_pages(pages)
	

	