# Automation tasks using Fabric
import fabric.api as fapi
import os

@fapi.task
def register():
	"""Registers a version of the package on pypi. Shouldn't need to run again."""
	fapi.local( 'python setup.py register' )

@fapi.task
def upload():
	"""Upload a new copy to pypi. Update the version in setup.py appropriately first."""
	docs()
	fapi.local( 'python setup.py sdist upload' )
	# No longer supported
	# fapi.local( 'python3 setup.py upload_docs --upload-dir=python3/shelljob/doc/_build' )
	
@fapi.task
def docs():
	#fapi.local( 'epydoc -v --html -o python3/shelljob/doc python3/shelljob' )
	fapi.local( 'sphinx-build -b html python3/shelljob/doc python3/shelljob/doc/_build' )
