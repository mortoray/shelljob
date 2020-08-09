import sys

from shelljob import proc

def test_group():
	sp = proc.Group()

	for i in range(0,5):
		sp.run( ['ls', '-al', '/usr/local'], encoding='utf-8' )
	while sp.is_pending():
		lines = sp.readlines()
		for pc, line in lines:
			if not isinstance(line,str):
				raise Exception("Expecting string") # since encoding specified
			sys.stdout.write( "{}:{}".format( pc.pid, line ) )
			

def test_unicode_group():
	sp = proc.Group()
	failed = False
	def on_error(e):
		nonlocal failed
		failed = True
		assert isinstance(e, UnicodeDecodeError)
		
	sp.run( ['cat', 'UTF-8-test.txt'], encoding='utf-8', on_error=on_error)
	while sp.is_pending():
		lines = sp.readlines()
		for pc, line in lines:
			print(line)
			
	assert failed
			
# added to test https://bugs.launchpad.net/mortoray.com/+bug/1872849
if __name__ == '__main__':
	test_unicode_group()
	#count = 0
	#while True:
		#test_group()
		#print(count)
		#count += 1
