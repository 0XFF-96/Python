import threading

def hello(name):

	# get_ident()  get the function 's threading id

	print('child thread: {}'.format(threading.get_ident()))

	print('Hello ' + name)


def main():

	#initial the threading , for delivery the parameter  as the processs

	t = threading.Thread(target=hello, args=('shiaynlou',))

	# start the threading and waiting  for it's dying 

	t.start()
	t.join()

	print('main thread: {}'.format(threading.get_ident()))

if __name__=='__main__':
	
	main()


