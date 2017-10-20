import time 
from multiprocessing import Process, Value

def func(val):
	
	for i in range(50):

		time.sleep(0.01)
		val.value +=1

if __name__=='__main__':

	# mutiprocessing can't use global variable.
	# Value is an agent 
	#for sharing the Varialbe between different Processes

	v = Value('i', 0)

	procs = [Process(target=func,args(v,)) for i in range(10)]

	for p in procs:
		
		p.start()
	
	for p in proces:
		
		p.join()

	print(v.value)


