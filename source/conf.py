# -*- coding: utf-8 -*-
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

from sphinx_antmicro_theme import __version__, get_html_theme_path
html_theme_path = ['.']
theme_path = get_html_theme_path() + "/sphinx_antmicro_theme"

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.8'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.todo',
              'sphinx.ext.ifconfig',
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.napoleon']
autodoc_mock_imports = ['cocotb', 'wishbone']
numfig = True
todo_include_todos=False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'USB test suite - guide'
basic_filename = u'usb-test-suite--guide'
authors = u'Antmicro'
copyright = authors + u', 2019'

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_antmicro_theme'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = theme_path+'/logo-400-html.png'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = today_fmt

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# Output file base name for HTML help builder.
htmlhelp_basename = basic_filename

try: html_context
except: html_context = {}
html_context['basic_filename'] = basic_filename

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', basic_filename+'.tex', project,
   authors, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = theme_path+'/logo-400.png'

man_pages = [
    ('index', basic_filename, project,
     [authors], 1)
]

latex_additional_files = ['%s/%s.sty' % (theme_path,html_theme),latex_logo]

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'fontpkg': r'''
        \usepackage{charter}
        \usepackage[defaultsans]{lato}
        \usepackage{inconsolata}
        \usepackage{lscape}
    ''',
    'preamble': r'''
          \usepackage{%s}
          \usepackage{multicol}
    ''' % html_theme,
    'maketitle': r'''
        \renewcommand{\releasename}{}
        \renewcommand{\sphinxlogo}{\includegraphics[height=75pt]{logo-400.png}\par}
        \sphinxmaketitle
    ''',
    'classoptions':',openany,oneside',
    'babel': r'''
          \usepackage[english]{babel}
          \makeatletter
          \@namedef{ver@color.sty}{}
          \makeatother
          \usepackage{silence}
          \WarningFilter{Fancyhdr}{\fancyfoot's `E' option without twoside}
    '''
}

rst_prolog = """
.. role:: raw-latex(raw)
   :format: latex

.. role:: raw-html(raw)
   :format: html
"""

rst_epilog = """
.. |project| replace:: %s
""" % project
