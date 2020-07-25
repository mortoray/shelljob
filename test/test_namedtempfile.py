import os
from shelljob import fs, proc

def test_basic():
	with fs.NamedTempFile() as nm:
		name = nm
		f = open(nm,"w")
		f.write( "Hello" )
		f.close()
		print( nm )
		
		f = open(nm,"r")
		assert f.read() == "Hello"
		
	assert not os.path.exists(name)

def test_affix():
	with fs.NamedTempFile( prefix = 'PRE', suffix = '.END' ) as nm:
		assert nm.find( 'PRE' ) > 0 # can't be first due to directory
		assert nm.endswith( '.END' )
		name = nm
	assert not os.path.exists(name)

def test_exception():
	# ensure deleted on exception
	try:
		with fs.NamedTempFile() as nm:
			name = nm
			raise Exception("oops")
	except Exception as e:
		assert not os.path.exists(name)

def test_example():
	# Example from docs
	with fs.NamedTempFile() as nm:
		proc.call( "curl http://mortoray.com/ -o {}".format( nm ) )
		html = open(nm,'r').read()
		print( len(html) )
		
		name = nm
	assert not os.path.exists(name)
