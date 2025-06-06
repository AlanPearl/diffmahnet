# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from pkg_resources import get_distribution

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
try:
    __version__ = get_distribution("diffmahnet").version
except:  # noqa
    __version__ = "unknown version"

project = 'diffmahnet'
copyright = '2025, Alan Pearl'
author = 'Alan Pearl'
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "myst_parser",
    "sphinx_copybutton",
]

templates_path = ['_templates']
exclude_patterns = [".ipynb_checkpoints/*"]
language = "Python"
master_doc = "index"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'nature'
html_theme = "sphinx_rtd_theme"
# html_static_path = ['_static']


# Don't show class signature in the header -- only in __init__
# autodoc_class_signature = "separated"
