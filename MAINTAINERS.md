## Virtual Environment

Typical `python3.6 -m venv env`

Add `src` to the virtual env.

In 'activate':

```
export PYTHONPATH=/src/shelljob/src/
```

## Local install for development/testing

```
pip3 install -e .
```

To Remove:

```
cd /usr/local/lib/python2.7/dist-packages
rm shelljob.egg-link
```

Also remove from easy-install.pth
