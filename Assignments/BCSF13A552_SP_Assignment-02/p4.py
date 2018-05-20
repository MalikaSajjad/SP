######a python script that displays detailed info of a given process by using the PID(s) (passed as command line argument(s)

import psutil 
import sys
import os
import time

try :
	p = psutil.Process(int(sys.argv[1]))
except:
	print "no sufficient args"
else:
	print "process ID: ", p.pid
	print "process Name: ", p.name
	print "process Status: ", p.status
	print "process Parent ID: ", p.ppid
	print "process Parent Name: ", psutil.Process(p.ppid).name
	print "Process Creation Time:", time.ctime(p.create_time)
	print "Files opened by the process info:", p.get_open_files()
	print "Memory Info (In Bytes):", p.get_memory_info()


#if __name__ == __main__:	
