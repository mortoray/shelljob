## Virtual Environment

Typical `python3.6 -m venv env`

Add `src` to the virtual env.

In 'activate':

```
export PYTHONPATH=/src/shelljob/src/
```

Then install requirements for development:

```
source env/bin/activate
pip install -r dev_requirements.txt
```

## Local install for development/testing

```
python3.6 -m venv env
source env/bin/activate
pip install pytest
pip install -e /src/shelljob
pytest /src/shelljob/test
```

