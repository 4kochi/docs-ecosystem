# -*- coding: utf-8 -*-
#
# MongoDB documentation build configuration file, created by
# sphinx-quickstart on Mon Oct  3 09:58:40 2011.
#
# This file is execfile()d with the current directory set to its containing dir.

import sys
import os.path
import datetime

project_root = os.path.join(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(project_root)

from bootstrap import buildsystem

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), buildsystem, 'sphinxext')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), buildsystem, 'bin')))

from utils import ingest_yaml, ingest_yaml_list
from docs_meta import get_conf, get_versions, get_manual_path

conf = get_conf()
pdfs = ingest_yaml_list(os.path.join(conf.build.paths.builddata, 'pdfs.yaml'))
intersphinx_libs = ingest_yaml_list(os.path.join(conf.build.paths.builddata, 'intersphinx.yaml'))

# -- General configuration ----------------------------------------------------

needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'mongodb',
    'directives',
    'intermanual'
]

templates_path = ['.templates']
exclude_patterns = []

source_suffix = '.txt'

master_doc = 'contents'
language = 'en'
project = u'mongodb-ecosystem'
copyright = u'2011-' + str(datetime.date.today().year) + ', MongoDB, Inc.'

version = '2.2.2'
release = version

BREAK = '\n'
rst_epilog = ('.. |branch| replace:: ``' + conf.git.branches.current + '``' + BREAK +
              '.. |copy| unicode:: U+000A9' + BREAK +
              '.. |year| replace:: ' + str(datetime.date.today().year) + BREAK +
              '.. |ent-build| replace:: MongoDB Enterprise' + BREAK +
              '.. |hardlink| replace:: http://docs.mongodb.org/' + conf.git.branches.current)

extlinks = {
    'issue': ('https://jira.mongodb.org/browse/%s', '' ),
    'wiki': ('http://www.mongodb.org/display/DOCS/%s', ''),
    'api': ('http://api.mongodb.org/%s', ''),
    'source': ('https://github.com/mongodb/mongo/blob/master/%s', ''),
    'docsgithub' : ( 'http://github.com/mongodb/docs/blob/' + conf.git.branches.current + '/%s', ''),
    'hardlink' : ( 'http://docs.mongodb.org/' + conf.git.branches.current + '/%s', ''),
    'manual': ('http://docs.mongodb.org/manual%s', ''),
    'ecosystem': ('http://docs.mongodb.org/ecosystem%s', ''),
    'meta-driver': ('http://docs.mongodb.org/meta-driver/latest%s', ''),
    'about': ('http://www.mongodb.org/about%s', '')
}

intersphinx_mapping = {}
for i in intersphinx_libs:
    intersphinx_mapping[i['name']] = ( i['url'], os.path.join('..', '..', i['path']))

languages = [
    ("ar", "Arabic"),
    ("cn", "Chinese"),
    ("cs", "Czech"),
    ("de", "German"),
    ("es", "Spanish"),
    ("fr", "French"),
    ("hu", "Hungarian"),
    ("id", "Indonesian"),
    ("it", "Italian"),
    ("jp", "Japanese"),
    ("ko", "Korean"),
    ("lt", "Lithuanian"),
    ("pl", "Polish"),
    ("pt", "Portuguese"),
    ("ro", "Romanian"),
    ("ru", "Russian"),
    ("tr", "Turkish"),
    ("uk", "Ukrainian")
]

# -- Options for HTML output ---------------------------------------------------

html_theme = 'mongodb'
html_theme_path = [ os.path.join(buildsystem, 'themes') ]
html_title = "MongoDB Ecosystem"
htmlhelp_basename = 'MongoDBdoc'

html_logo = ".static/logo-mongodb.png"
html_static_path = ['source/.static']
html_last_updated_fmt = '%b %d, %Y'

html_copy_source = False
html_use_smartypants = True
html_domain_indices = True
html_use_index = True
html_split_index = False
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True

manual_edition_path = 'http://docs.mongodb.org/ecosystem/MongoDB-Ecosystem'

html_theme_options = {
    'branch': conf.git.branches.current,
    'pdfpath': manual_edition_path + '.pdf',
    'epubpath': manual_edition_path + '.epub',
    'manual_path': get_manual_path(conf),
    'translations': languages,
    'language': language,
    'repo_name': 'docs-ecosystem',
    'jira_project': 'DOCS',
    'google_analytics': 'UA-7301842-8',
    'project': 'ecosystem',
    'version': version,
    'version_selector': get_versions(conf),
    'stable': conf.version.stable,
}

html_sidebars = {
    '**': ['pagenav.html'],
}
html_sidebars['**'].append('intrasites.html')
# html_sidebars['**'].append('translations.html')
html_sidebars['**'].append('resources.html')

# -- Options for LaTeX output --------------------------------------------------

latex_documents = []
for pdf in pdfs:
    _latex_document = ( pdf['source'], pdf['output'], pdf['title'], pdf['author'], pdf['class'])
    latex_documents.append( _latex_document )

latex_elements = {
    'preamble': '\DeclareUnicodeCharacter{FF04}{\$} \DeclareUnicodeCharacter{FF0E}{.} \PassOptionsToPackage{hyphens}{url}',
    'pointsize': '10pt',
    'papersize': 'letterpaper'
}

latex_paper_size = 'letter'
latex_use_parts = True
latex_show_pagerefs = True
latex_show_urls = False
latex_domain_indices = True
latex_logo = None
latex_appendices = []

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'MongoDB'
epub_author = u'MongoDB Documentation Project'
epub_publisher = u'MongoDB Documentation Project'
epub_copyright = copyright
epub_theme = 'epub_mongodb'
epub_tocdup = True
epub_tocdepth = 3
epub_language = 'en'
epub_scheme = 'url'
epub_identifier = 'http://docs.mongodb.org/ecosystem/'
epub_exclude_files = []
epub_pre_files = []
epub_post_files = []
