import os
import sys


sys.path.insert(0, os.path.abspath(os.path.join('..', '..', 'django')))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'steph'
copyright = '2025, pebble'
author = 'pebble'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints', 
    'sphinxcontrib_django',
]

autodoc_member_order = 'bysource'

autodoc_default_options = {
    'members': True,  # члены
    'undoc-members': True,  # члены
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
