

## Synchronization create problem !!

import threading
from time import sleep
import os, random 

# 
numPhilosophers = numForks = 2

class Philosopher(threading.Thread):

	def __init__(self, index):

		threading.Thread.__init__(self)
		self.index = index
		self.leftFork = forks[self.index]
		
		self.rightFork = forks[(self.index + 1) % numForks]

	def run(self):

		while True:

			self.leftFork.pickup()
			self.rightFork.pickup()
			self.dinning()

			self.leftFork.putdown()
			self.rightFork.putdown()
			self.thinking()

	def dinning(self):

		print "philosopher", self.index, " starts to eat."

		sleep(random.uniform(1, 3)/1000)

		print "Philosopher", self.index, " finishes eating and leaves to think"

	
	def thinking(self):

		sleep(random.uniform(1,3)/1000)

class Fork():

	def __init__(self, index):

		self.index =index
		self._lock = threading.Lock()

	def pickup(self):
		
		self._lock.acquire()

	def putdown(self):

		self._lock.release()


if __name__=='__main__':

	forks = [Fork(idx) for idx in range(numForks)]

	philosophers = [Philosopher(idx) for idx in range(numPhilosophers)]

	# create all the threading

	for philosopher in philosophers:

		philosopher.start()

	# CTRL + C  exit()

	try:
		while True: sleep(0.1)
	except Exception, e:
		raise e


