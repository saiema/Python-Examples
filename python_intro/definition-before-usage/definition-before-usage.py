import sys

def foo(x: int) -> int:
	return 42 + x
	
if len(sys.argv) != 2:
	raise Exception("Expecting only one argument")
else:
	if not sys.argv[1].isdigit():
		raise Exception("Expecting a number")
	else:
		value: int = int(sys.argv[1])
		if value % 2 != 0:
			print(bar(value))
		else:
			print(foo(value))
	
