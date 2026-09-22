from __future__ import annotations

import os
import sys
from importlib.metadata import PackageNotFoundError, version as package_version

sys.path.insert(0, os.path.abspath("../src"))

project = "Trend Estimation"
author = "Heriberto Espino Montelongo"

try:
    release = package_version("trend-estimation")
except PackageNotFoundError:
    release = "development"

version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "bysource"
napoleon_google_docstring = True
napoleon_numpy_docstring = True

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "Trend Estimation"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
}
