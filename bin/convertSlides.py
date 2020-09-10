'''
Written by Danny Caballero
5 Sept 2020

This script will read a notebook filename and convert it to slides. It keeps the notebook and slides in different folders. Any images used in the notebook will be copied over to the slides folder.
'''

import sys
from subprocess import call

NOTEBOOK = sys.argv[1]
NOTEBOOKDIR = 'notebooks/'
HTMLDIR = 'docs/'
IMAGESDIR = 'images'

ext = NOTEBOOK.index(".ipynb")
newext = ".slides.html"

SLIDES = NOTEBOOK[:ext] + newext

call(["jupyter-nbconvert", NOTEBOOK, "--to", "slides"])

call(["mv", SLIDES, HTMLDIR])
call(["cp", "-r", NOTEBOOKDIR + IMAGESDIR, HTMLDIR])
