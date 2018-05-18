try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Automated Testing with Python - LPTHW3 ex47',
	'author': 'Saad Mashkoor Siddiqui',
	'url': '',
	'download_url': '',
	'author_email': 'saadsiddiqui.ned16@gmail.com',
	'version' : '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'ex47'
}