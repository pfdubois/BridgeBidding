# -*- coding: utf-8 -*-
#
# To see the choices go to sphinx-doc.org.   
project = u'BridgeBidding'
booktitle = u'Bridge Bidding'
bookshorttitle = u'Bridge Bidding'

# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = ' '

# -*- coding: utf-8 -*-
sproject = project.replace(' ','')

import sphinx.util.texescape as te
needs_sphinx = '9.0'  ### ha ha ha when I started it was 1.9; no idea really
copyright = '2024, Paul F. Dubois' 
author = 'Paul F. Dubois'
language = 'en'
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False
#The github one generates a .nojekyll file in the html so that my own theme is used
#on github
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '_ext')))

extensions = ['sphinx.ext.ifconfig','sphinx.ext.githubpages','sphinx.ext.extlinks',
              'bridgedeal']
# Where :website:`file` links will point to. None means show link explicitly
extlinks = { 'website':('https://pfdubois.github.io/BridgeBidding/%s',None)}

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']
source_suffix = {'.rst': 'restructuredtext'}

# The master toctree document.
master_doc = 'index'

# HTML
html_theme = 'classic'
html_title = booktitle
html_short_title = bookshorttitle
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True
html_static_path = ['_static']
#
# PDF
#
latex_engine = 'xelatex'
papersize ='letter'
latex_documents = [
    (master_doc, sproject+'.tex', booktitle, author, 'manual', False),
]
latex_show_pagerefs = True

# This used to be needed to get the suit symbols black and white. Now (2026) it 
# just works with xelatex. You do get two harmless error messages about U+FE0E
# at the end of the make. 

# te.tex_replacements += [
#     ['♥', r'\ensuremath{\heartsuit}'],
#     ['♣', r'\ensuremath{\clubsuit}'],
#     ['♦', r'\ensuremath{\diamondsuit}'],
#     ['♠', r'\ensuremath{\spadesuit}']
#     ]
# te.init()

# Can also change this to use a4paper or letter, and make it one column if
# desired by removing \twocolumn to the preamble

my_preamble = r'''
\usepackage{unicode-math}
\pagenumbering{arabic}
\pagestyle{headings}
\setlength{\headheight}{14.0pt}
\setcounter{secnumdepth}{0}
\definecolor{TitleColor}{rgb}{0,0,0}
\definecolor{InnerLinkColor}{rgb}{0,0,0}
\definecolor{OuterLinkColor}{rgb}{0,0,0}
\twocolumn
'''

latex_elements = {
   'pointsize': '11pt',
   'papersize': papersize,
   'sphinxsetup':'hmargin={1in, 0.5in}, vmargin = {0.75in, 0.75in}',
   'preamble': my_preamble,
   'releasename': ' ',
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
latex_show_pagerefs = True
latex_show_urls = 'inline'
#
#EPUB
#
# Bibliographic Dublin Core info.
epub_title = "Bridge Bidding"
epub_description = "A guide to bridge bidding for intermediate to advanced players"
epub_author = author
epub_publisher = author
epub_language = "English"
epub_copyright = copyright
epub_scheme = "URL"
epub_cover = ('_static/cover-kdp.jpg', 'epub-cover.html')
epub_tocdepth = 2
# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
epub_identifier = 'pfdubois.github.io/BridgeBidding'

# A unique identification for the text.
#
epub_uid = project

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# Sphinx already writes genindex.xhtml and places it at the end of the
# reading order, but it does not put that page in nav.xhtml or toc.ncx.
# This is the supported way to add one contents entry for it. HTML and
# LaTeX ignore this setting; the PDF keeps its own index.
epub_post_files = [('genindex.xhtml', 'Index')]

# EPUB 2 guide entry. Apple Books still reads this for its Go To menu.
# The automatic "toc" guide entry is left in place.
epub_guide = [('index', 'genindex.xhtml', 'Index')]


# HTML pages only (not EPUB, which is built by a subclass of the HTML builder):
# add _static_html/custom.css, which makes 3rd- and 4th-level headings smaller.
def _html_only_css(app):
    if app.builder.name in ('html', 'dirhtml', 'singlehtml'):
        app.config.html_static_path.append('_static_html')
        app.add_css_file('custom.css')
    # The deal box is wanted in the EPUB as well. custom.css stays HTML-only.
    if app.builder.name in ('html', 'dirhtml', 'singlehtml', 'epub'):
        app.add_css_file('bridge-deal.css')


def _epub_index_packaging(app):
    """EPUB-only packaging fixes. HTML and LaTeX builders never get here."""
    if app.builder.name != 'epub':
        return
    builder = app.builder
    original_content = builder.build_content
    original_toc = builder.build_toc
    original_nav = builder.build_navigation_doc

    def build_content():
        # epub_post_files lists genindex for the contents menus. The builder
        # also appends that page to the reading order, so drop it here to
        # keep a single turn of the page.
        kept = builder.refnodes
        builder.refnodes = [
            node for node in kept
            if not str(node.get('refuri', '')).startswith('genindex')
        ]
        try:
            original_content()
        finally:
            builder.refnodes = kept

    def build_toc():
        # NCX dtb:uid must equal the OPF identifier text. Sphinx writes
        # epub_uid there instead, and that value is the XML id "BridgeBidding".
        # The published identifier stays pfdubois.github.io/BridgeBidding;
        # only this one NCX field is aligned with it, after content.opf
        # has already been written.
        saved = builder.config.epub_uid
        builder.config.epub_uid = builder.config.epub_identifier
        try:
            original_toc()
        finally:
            builder.config.epub_uid = saved

    def build_navigation_doc():
        original_nav()
        # Landmarks are what Apple Books uses for Go To, in addition to the
        # table of contents. hidden keeps this menu out of the page flow.
        path = builder.outdir / 'nav.xhtml'
        text = path.read_text(encoding='utf-8')
        if 'epub:type="landmarks"' in text:
            return
        landmark = (
            '    <nav epub:type="landmarks" hidden="">\n'
            '      <h2>Landmarks</h2>\n'
            '      <ol>\n'
            '        <li><a epub:type="index" href="genindex.xhtml">Index</a></li>\n'
            '      </ol>\n'
            '    </nav>\n'
        )
        path.write_text(text.replace('</body>', landmark + '  </body>'), encoding='utf-8')

    original_write = builder.write_doc

    def write_doc(docname, doctree):
        original_write(docname, doctree)
        # Apple Books shows this page as the contents inside the book.
        # The chapter list is filled in only while the page is written,
        # which is after doctree-resolved, so the link is added here.
        if docname != builder.config.master_doc:
            return
        path = builder.outdir / (docname + builder.out_suffix)
        text = path.read_text(encoding='utf-8')
        if 'href="genindex.xhtml"' in text:
            return
        marker = '</ul>\n</div>'
        insert = (
            '<li class="toctree-l1">'
            '<a class="reference internal" href="genindex.xhtml">Index</a>'
            '</li>\n'
        )
        if marker not in text:
            return
        path.write_text(
            text.replace(marker, insert + marker, 1),
            encoding='utf-8',
        )

    builder.build_content = build_content
    builder.build_toc = build_toc
    builder.build_navigation_doc = build_navigation_doc
    builder.write_doc = write_doc


def setup(app):
    app.connect('builder-inited', _html_only_css)
    app.connect('builder-inited', _epub_index_packaging)
