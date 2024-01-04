# import os
# import sys
# import django

# pour aller chercher les modules et récupérer les docstrings (voir extensions ci-dessous)
# sys.path.insert(0, os.path.abspath("../.."))
# os.environ["DJANGO_SETTINGS_MODULE"] = "oc_lettings_site.settings"
# django.setup()


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Orange County Lettings"
copyright = "2023, Mathieu Cazenave - OC-Formation Python- Projet 13"
author = "Mathieu Cazenave"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# extensions pour docstrings (dont napoleon qui prend en charge langage google)
# extensions = [
# "sphinx.ext.autodoc",
# "sphinx.ext.coverage",
# "sphinx.ext.napoleon",
# ]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "fr"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "display_version": False,
    "style_external_links": True,
}
html_logo = "_static/logo.png"
html_static_path = ["_static"]
