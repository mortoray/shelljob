# shelljob setup.py
import os,sys
from setuptools import setup

base_dir = 'src'

def list_files(path):
	m = []
	for root, dirnames, filenames in os.walk(path):
		for filename in filenames:
			m.append(os.path.join(root, filename))
	return m
			
setup(
	name = 'shelljob',
	packages = [ 'shelljob' ],
	package_dir = {
		'': base_dir,
	},
	version = '0.6.2',
	description = 'Run multiple subprocesses asynchronous/in parallel with streamed output/non-blocking reading. Also various tools to replace shell scripts.',
	author = 'edA-qa mort-ora-y',
	author_email = 'eda-qa@disemia.com',
	url = 'https://github.com/mortoray/shelljob/',
	classifiers = [
		'Development Status :: 6 - Mature',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Intended Audience :: Developers',
		'Environment :: Console',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Operating System :: OS Independent',
		'Topic :: Terminals',
		'Topic :: System',
		'Topic :: Software Development :: Build Tools',
		],
	long_description = open('README.md','r',encoding="utf-8").read(),
	long_description_content_type="text/markdown",
	package_data = { 
		'shelljob': [ base_dir + '/doc/*' ] 
	},
	license = 'GPLv3',
	python_requires=">=3.6",
)
