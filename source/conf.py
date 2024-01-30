# -*- coding: utf-8 -*-
#
project = u'BridgeBidding'

# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0a'

# -*- coding: utf-8 -*-
sproject = project.replace(' ','')

import sphinx.util.texescape as te
needs_sphinx = '1.9'
copyright = u'2024, Paul F. Dubois'
author = u'Paul F. Dubois'
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False
# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'http://pfdubois.com/publish/': None}
#extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.ifconfig']
#The github one generates a .nojekyll file in the html so that my own theme is used
#on github
extensions = ['sphinx.ext.ifconfig','sphinx.ext.githubpages','sphinx.ext.extlinks']
# Where :website:`file` links will point to. None means show link explicitly
extlinks = { 'website':('https://pfdubois.github.com/BridgeBidding/%s',None)}

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']
source_suffix = {'.rst': 'restructuredtext'}

# The master toctree document.
master_doc = 'index'

# HTML
html_theme = 'classic'
html_title = 'A Guide To Bridge Bidding'
html_short_title = 'Bridge Bidding'
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
#
# PDF
#
latex_documents = [
    (master_doc, sproject+'.tex', project,
     author, 'manual'),
]


te.tex_replacements += [
    ['♥', r'\ensuremath{\heartsuit}'],
    ['♣', r'\ensuremath{\clubsuit}'],
    ['♦', r'\ensuremath{\diamondsuit}'],
    ['♠', r'\ensuremath{\spadesuit}']
    ]
te.init()

# Can also change this to use a4paper or letter, and make it two columns if
# desired by adding \twocolumn to the preamble
# Could make selectable via env variables ?
my_preamble = r'''
\usepackage[utf8]{inputenc}
\pagenumbering{arabic}
\pagestyle{plain}
\setcounter{secnumdepth}{1}
\setcounter{tocdepth}{1}
\definecolor{TitleColor}{rgb}{0,0,0}
\definecolor{InnerLinkColor}{rgb}{0,0,0}
\definecolor{OuterLinkColor}{rgb}{0,0,0}
'''
latex_elements = {
   'pointsize': '11pt',
   'papersize': 'a5paper',
   'preamble': my_preamble,
   'releasename': '',
   'classoptions': ',openany,oneside',
   'babel':'\\usepackage[english]{babel}',
   'maketitle':r'''\newcommand\sphinxbackoftitlepage{
   
   
Copyright, 2010-2024, Paul F. Dubois

This book is non-commercial and meant for free redistribution to other 
bridge players. It is licensed under the GNU GPLv3 license.
You can see a copy of this license at 

https://spdx.org/licenses/GPL-3.0-or-later.html

}\sphinxmaketitle
'''
}
 

# The last two get rid of blank pages
#latex_elements['classoptions'] = ',openany,oneside'
#latex_elements[ 'babel'] = '\\usepackage[english]{babel}'

# If false, no module index is generated.
latex_domain_indices = False
latex_domain_indices = False
latex_show_pagerefs = True
latex_show_urls = 'inline'
#
#EPUB
#
# Bibliographic Dublin Core info.
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_tocdepth = 2
# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
epub_identifier = 'pfdubois.com/publish/'

# A unique identification for the text.
#
epub_uid = project

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


