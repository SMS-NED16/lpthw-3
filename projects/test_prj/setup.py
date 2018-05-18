try:
	from setuptools import setuptools
except ImportError:
	from distutils.core import setup

config = {
	'description': 'A test project written for Required Quiz 46, LPTHW-3',
	'author': 'Saad Mashkoor Siddiqui',
	'url': '',
	'download_url': '',
	'author_email': 'saadsiddiqui.ned16@gmail.com',
	'version' : '0.1',
	'install_requires': ['nose'],
	'packages': ['test_prj'],
	'scripts': ['test_script'],
	'name': 'test_prj'
}