#!/bin/python
# -*- coding: utf-8 -*-
import os
import os.path
import sys
import codecs
import yaml
import json
import string
import fnmatch
import markdown
import mistune
import jinja2
from glob import glob
from md2json import md2dict, md2json
from distutils.dir_util import mkpath


config_index_file = 'index.yml'

config_pages_dir = '_pages'
config_page_ext = '.md'

config_build_dir = '_build'
config_build_ext = 'db.json'

index_data = dict()



def load_config(filename):
	data = dict()
	with codecs.open(filename, 'r', 'utf8') as f:
		text = f.read()
		data = yaml.load(text)
	return data


def load_from_dir(folder, extension):
	matches = []
	for root, dirnames, filenames in os.walk(folder):
		for filename in fnmatch.filter(filenames, '*'+extension):
			matches.append(os.path.join(root, filename))
	return matches


def get_available_pages():
	return load_from_dir(folder=config_pages_dir, extension=config_page_ext)


def load_page_item(item, path):
	print "load_page_item", item
	if type(item) is dict:
		return load_page_dict(item, path)
	elif type(item) is list:
		return load_page_list(item, path)
	else:
		return load_page(item, path)

def load_page_dict(data, path):
	cv_data = []
	for k in data.keys():
		item = load_page_item(data[k], os.path.join(path, k))
		if item:
			cv_data += item
	return cv_data

def load_page_list(data, path):
	cv_data = []
	for item in data:
		if item:
			doc = load_page_item(item, path)
			if doc:
				cv_data += doc
	return cv_data


def load_page(page, path):
	if page:
		print "str", page
		page_path = os.path.join(config_pages_dir, page)
		if os.path.exists(page_path):
			doc = load_page_contents(page_path)
			docpath = os.path.join(path, codecs.encode(doc["config"]["title"], "utf-8"))
			print "path", docpath, page
			return docpath, doc

def load_pages(data):
	return load_page_item(data, path="")


def load_page_contents(page_path):
	print page_path
	with codecs.open(page_path, 'r', 'utf8') as f:
		text = f.read()
		d = md2dict(text)
		return convert_page_dict(d)


def convert_page_dict(pagedict):
	htmlPage = ""
	if pagedict["config"] and pagedict["content"]:
		return pagedict


def convert_page(page):
	d = dict()
	target = page.replace(config_pages_dir, config_build_dir).replace(config_page_ext, config_build_ext)
	htmlPage = ""
	with codecs.open(page, 'r', 'utf8') as f:
		text = f.read()
		d = md2dict(text)
		htmlPage = convert_page_dict(d)
	mkpath(os.path.dirname(target))
	with codecs.open (target, 'wb', 'utf8') as ff:
		ff.write(htmlPage)





def convert_pages(pages):
	for p in pages:
		convert_page(p)


if __name__ == '__main__':
	print "available pages", get_available_pages()
	index_data = load_config(config_index_file)
	print index_data["content"]

	pages = load_pages(index_data["content"])
	print pages

	converted = json.dumps(pages, sort_keys=True, indent=4, separators=(',', ': '))
	mkpath(os.path.dirname(config_build_dir))
	target = os.path.join(config_build_dir, config_build_ext)
	with codecs.open (target, 'w', 'utf8') as ff:
		ff.write(converted)
