test:
	#!/bin/bash
	source env/bin/activate
	export PYTHONPATH={{invocation_directory()}}/src/
	cd test
	python -m pytest .

docs:
	#!/bin/bash
	source env/bin/activate
	python -m sphinx doc-in docs
	touch docs/.nojekyll


upload:
	rm -fr dist
	python setup.py bdist_wheel
	twine upload dist/*.whl 
	
	
register:
	python setup.py register

freeze:
	pip freeze > dev_requirements.txt
