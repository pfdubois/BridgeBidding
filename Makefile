
# Makefile for Sphinx documentation
#
# How to use it:
#
#   make all       Build html, text, pdf and epub into build/ only.
#                  Use this any time to check that the book builds.
#                  It never touches docs/.
#
#   make install   Empty docs/ and refill it from what is in build/.
#
#   make publish   Do "make all" and then "make install". Use this
#                  before every commit, then "git add docs".
#
#   make hooks     Run this once on each computer. It turns on a check
#                  that stops "git commit" if build/ is newer than docs/
#                  (that is, if you forgot "make install"). The check
#                  itself is the script tools/pre-commit.
#                  To commit anyway, use: git commit --no-verify
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build

# Internal variables.
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) source
PUBLISH = docs
PUBNAME = BridgeBidding
EPUB = build/epub/BridgeBidding.epub
#CLEAN_EPUB = build/epub/BridgeBiddingX.epub
#EBOOK_CONVERT_PATH = /Applications/calibre.app/Contents/MacOS/ebook-polish

.PHONY: help clean all install publish hooks html dirhtml singlehtml epub latex latexpdf text man linkcheck 

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  all        to build html, text, pdf and epub into build/ (docs untouched)"
	@echo "  install    to replace docs/ with the outputs already in build/"
	@echo "  publish    to do all, then install (use this before committing)"
	@echo "  hooks      to install the git pre-commit check on this computer"
	@echo "  html       to make standalone HTML files"
	@echo "  dirhtml    to make HTML files named index.html in directories"
	@echo "  singlehtml to make a single large HTML file"
	@echo "  epub       to make an epub"
	@echo "  latex      to make LaTeX files"
	@echo "  latexpdf   to make LaTeX files and run them through pdflatex"
	@echo "  text       to make text files"
	@echo "  linkcheck  to check all external links for integrity"

clean:
	rm -rf $(BUILDDIR)

all: clean html text latexpdf epub

publish: all install

hooks:
	cp tools/pre-commit .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
	@echo "Installed the pre-commit check in .git/hooks."

install:
	rm -fr $(PUBLISH)
	mkdir $(PUBLISH)
	cp .nojekyll $(PUBLISH)/.nojekyll
	cp -R build/html/* $(PUBLISH)
	cp -f build/epub/$(PUBNAME).epub $(PUBLISH)/$(PUBNAME).epub
	cp -f build/latex/$(PUBNAME).pdf $(PUBLISH)/$(PUBNAME).pdf
	cp -R build/text $(PUBLISH)/$(PUBNAME)Chapters
	zip -r -q $(PUBNAME) build/* && mv $(PUBNAME).zip $(PUBLISH)/$(PUBNAME).zip
	cd $(PUBLISH) && zip -r -q $(PUBNAME)Chapters $(PUBNAME)Chapters
	cd $(PUBLISH) && rm -fr $(PUBNAME)Chapters

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
#	@echo "Polishing EPUB with Calibre..."
#	$(EBOOK_CONVERT_PATH) "$(EPUB)" "$(CLEAN_EPUB)" \
#	  -u \
#	  --add-soft-hyphens \
#	  || echo "ebook-polish failed — ensure calibre tools are in PATH"
#	@echo
	@echo "Build finished. The epub file is in $(BUILDDIR)/epub."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	make -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

doctest:
	$(SPHINXBUILD) -b doctest $(ALLSPHINXOPTS) $(BUILDDIR)/doctest
	@echo "Testing of doctests in the sources finished, look at the " \
	      "results in $(BUILDDIR)/doctest/output.txt."

