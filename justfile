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
	python setup.py bdist_wheel
	twine upload dist/*.whl dist/*.gz
	
	
register:
	python setup.py register

freeze:
	pip freeze > dev_requirements.txt
