#! /bin/python

'''
The MIT License (MIT)

Copyright (c) 2014 Santosh Sahoo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
import sys
import shutil
import json
from jinja2 import Template, Environment, FileSystemLoader

model  = json.load(open('pinku.json'))

def main():
	rootdir = 'templates'
	destdir = '../www'

	os.chdir(rootdir)
	if not os.path.exists(destdir): os.mkdir(destdir)
	env = Environment(loader=FileSystemLoader('.'))

	fileList = []
	for root, subFolders, files in os.walk('.'):
		dirname = os.path.join(destdir, root)
		if not os.path.exists(dirname):
			print 'mkdir:', dirname
			os.mkdir(dirname)

		for file in files:
			filename = os.path.join(root,file)
			filepath, ext = os.path.splitext(filename)
			if ext == '.tmpl':
				template = env.get_template(filename)
				output_from_parsed_template = template.render(**model)
				destfilename = os.path.join(destdir, filepath)
				with open(destfilename, "wb") as fh:
					fh.write(output_from_parsed_template)
			elif ext == '.ignore':
				continue
			else:
				shutil.copy2(filename, os.path.join(destdir, filename))

if __name__ == '__main__':
	main()