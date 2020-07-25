# shelljob

This provides a clean way to execute subprocesses, either one or multiple in parallel, capture their output and monitor progress:

- Single sub process `call` with optional timeout
- High level `FileMonitor` to execute several processes in parallel and store output in a file
- Low level `Group` execution to execute jobs in parallel and capture output

Additional tools for working with the filesystem are also included: 

- `find` which offers much of the functionality of the shell find utility
- `shelljob.fs.NamedTempFile` provides a _with_ block wrapper for temporary named files

[API Documentation](https://mortoray.github.io/shelljob/)


# Install

```
pip install shelljob
```

# Parallel Subprocesses

Using the Job system is the quickest approach to just run processes and log their output (by default in files named '/tmp/job_ID.log')

````
from shelljob import job

jm = job.FileMonitor()
jm.run([
	[ 'ls', '-alR', '/usr/local' ],
	'my_prog',
	'build output input',
])
````

An array will passed directly to `subprocess.Popen`, a string is first parsed with `shlex.split`.

The lower level `Group` class provides a simple container for more manual job management.

````
from shelljob import proc

g = proc.Group()
p1 = g.run( [ 'ls', '-al', '/usr/local' ] )
p2 = g.run( [ 'program', 'arg1', 'arg2' ] )

while g.is_pending():
	lines = g.readlines()
	for proc, line in lines:
		sys.stdout.write( "{}:{}".format( proc.pid, line ) )
````

# Simple Subprocess calls

A simplified `call` function allows timeouts on subprocesses and easy acces to their output.

````
from shelljob import proc

# capture the output
output = proc.call( 'ls /tmp' )
# this raises a proc.Timeout exception
proc.call( 'sleep 10', timeout = 0.1 )
````

# Find

The 'find' funtion is a multi-faceted approach to generating listings of files.

````
from shelljob import fs

files = fs.find( '/usr/local', name_regex = '.*\\.so' )
print( "\n".join(files) )
````

Refer to the [API docs](https://mortoray.github.io/shelljob/) for all parameters. Just let me know if there is some additional option you need.


