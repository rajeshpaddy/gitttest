import sys
from time import time
from datetime import datetime as dt
def print_arg(url):
	"""
	print_arg(arl)
	
	Args:
		url is the thing that you want to pass
	"""
	print(url)

attempt=0
time_start=time()
time_end=time()
def find(array,value):
	global attempt
	global time_start
	global time_end
	attempt+=1	
	length=len(array)
#	print("length",length,array)
	if(attempt==1):
		time_end=time()
		if value not in array:
			print("No value")
			return		 
	if(length==1):
#		time_end=dt.now().microsecond
#		print (array)
		print ("attempt",attempt)
		print("ET {0} milliseconds".format(float(time_end-time_start)/1000))
		attempt=0
		return array
	mid = int(length/2)		
	if(value<array[mid]):
		print("left {0} attempt".format(attempt),array[:mid])
		find(array[:mid],value)
	else:
		print("right {0} attempt".format(attempt),array[mid:])
		find(array[mid:],value)
	
if __name__=="__main__":
	print_arg(sys.argv[1])