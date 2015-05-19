# SOL - a static web page generator in Python

SOL is intended as a minimal static web page generator written in Python.

## Dependencies

-   Markdown: python markdown renderer
-   Markdown-gfm: adds support for Github flavored Markdown to above renderer
-   Mistune: super fast renderer
-   PyYaml: used to load config files and YAML front matter of the markdown files
-   Jinja2: used for templating

Written for Python 2.x

## Usage

At the moment `convert.py` will do everything.

Markdown pages go into `_pages`.  
Jinja2 templates go into `_templates`.  
The resulting HTML pages will go into `_build`, keeping the filename of their originating markdown file.

## Extras

`json2yaml.py file.json` takes a JSON file and writes the equivalent YAML to stdout.  
`yaml2json.py file.yml` takes a YAML file and writes the equivalent JSON to stdout.  
`mltiyaml2json.py file.yml` takes a multidocument YAML file and writes the equivalent JSON containing each document as JSON string.  
`md2json.py file.md` takes a Markdown file with YAML front matter and writes the equivalent JSON to stdout, keeping the Markdown as port of the JSON.  

`mistune_test.py`is a short Mistune Markdown renderer test.  
`markdown_test.py`is a short Markdown-gfm renderer test.  
`jinja_test.py`is a short Jinja2 test.  
