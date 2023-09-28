# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "曹志成的"
copyright = ''
author = '曹志成'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    'navigation_depth': -1,
    "header_links_before_dropdown": 8
}
html_search_options = {'dict': '.venv/Lib/site-packages/jieba/dict.txt'}
# html_search_options = {'dict': 'c:/Users/Admin/AppData/Local/Programs/Python/Python37/Lib/site-packages/jieba/dict.txt'}

