import random, traceback

from shelljob import job, proc

def test_job():
	jm = job.FileMonitor(feedback_timeout = 0.5)

	cmds = [ [ 'ls', '-alR', '/usr/local/' ] for i in range(0,2) ]
	# plain strings can be used (note these 'ls' commands are expected to fail)
	cmds += [ 'ls -alR /usr/local/{}'.format(i) for i in range(0,5) ]
	# explicits Jobs can be created
	def gen_job(i):
		obj = job.Job( 'echo {}'.format(i) )
		obj.name = 'Echo #{}'.format(i)
		return obj
	cmds += [ gen_job(i) for i in range(0,10) ]

	random.shuffle(cmds)

	jm.run( cmds )

	
# https://bugs.launchpad.net/mortoray.com/+bug/1314597
def test_cmd_not_found():
	jm = job.FileMonitor()
	caught = False
	try:
		jm.run([
			[ 'ls', '-alR', '/usr/local' ],
			'my_prog',
		])
	except proc.CommandException as e:
		s = traceback.format_exc()
		assert s.find( 'my_prog' ) != -1
		assert s.find( 'FileNotFoundError' ) != -1
		caught = True
	assert caught