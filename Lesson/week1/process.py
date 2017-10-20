
import os

from multiprocessing import Process

def hello(name):
	print('Child process: {} '.format(os.getpid()))
	print('Hello ' + name)


def main():

	# args parameter shuold be tuple

	p = Process(target=hello, args=('shiyanlou', ))
	p.start()
	p.join()
	print('parent process: {}'.format(os.getpid()))

if __name__=='__main__':

	main()

	
