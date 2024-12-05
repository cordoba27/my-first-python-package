from setuptools import setup, find_packages
from pathlib import Path

# Requirements
try:
  this_directory = Path(__file__).absolute().parent
  with open((this_directory / "requirements.txt"), encoding = "utf-8") as f:
    requirements = f.readlines()
  requirements = [line.strip() for line in requirements]
except FileNotFoundError:
  requirements = []

# Metadata
setup(
  name = "bastipy",
  version = 0.0.0.9000,
  author = "Sebastian Schmidt",
  author_email = "sebastian.schmidt@plus.ac.at",
  description = "Count features in geofile.",
  license = "Type here what license your package has",
  packages = find_packages(),
  install_requires = requirements
)