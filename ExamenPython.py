
import time
import datetime
import threading


################################################################################
# 
################################################################################

Stock_1  = []
Stock_2  =  []
Tank_Fifo =[]
Tank_Oil = 0

class my_task():


	name = None
	priority = -1
	period = -1
	execution_time = -1
	use_oil = 0 
	global produce = None

    	############################################################################
	def __init__(self, name, priority, period,execution_time,use_oil,produce = None):

		self.name = name
		self.priority = priority
		self.period = period
		self.execution_time = execution_time
		self.use_oil = use_oil
		self.produce = None

def run(self):

	global Tank_Oil 

	while(0<Tank_Oil<50):

		
		if (self.priority == 1) :
		
			Tank_Fifo.append(datetime.datetime.now().strftime("%H:%M:%S") + "\t" 
				+ self.name + " : inside Tank : " + datetime.datetime.now().strftime("%H:%M:%S"))
			Tank_Oil =+ self.use_oil
		
		else :
			while (len(Stock_1 or Stock_2) > 0):
				print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" +  self.name + " : " + Stock_2[0] + Stock_1[0]
				) 
				
		if (my_task.produce : True):
			if my_task.name = "Machine_1"
				Stock_1.append(datetime.datetime.now().strftime("%H:%M:%S") + "\t" 
							+ self.name + " : WHEELS STOCK : " + datetime.datetime.now().strftime("%H:%M:%S"))
			else:
				Stock_2.append(datetime.datetime.now().strftime("%H:%M:%S") + "\t" 
						+ self.name + " : MOTORS STOCK : " + datetime.datetime.now().strftime("%H:%M:%S"))


		
		time.sleep(self.execution_time)
		print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : blocked ")
		time.sleep(self.period - self.execution_time)

####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

	

	# Instanciation of task objects
	task_list = []
	nb_wheels = 0
	nb_motors = 0
	task_list.append(my_task(name="Pump_1", priority = 1, period = 5, execution_time = 2,use_oil =+10,produce=False ))
	task_list.append(my_task(name="Pump_2 ", priority = 1, period = 15, execution_time = 3,use_oil =+20,produce=False))
	task_list.append(my_task(name="Machine_1", priority = 2, period = 5, execution_time = 5,use_oil= -25,produce=True,nb_wheels=+1 ))
	task_list.append(my_task(name="Machine_2", priority = 2, period = 5, execution_time = 3,use_oil= -5,produce=True),nb_motors=+1)


for task in task_list :
	
	if (Tank_Oil>= Tank_Oil - my_task.use_oil):
		if (nb_wheels / 4) > nb_motors & my_task.name = "Machine_1":
				priority = 3
	task.start()


		