class Event :

	# stores the details of the event
	
	def __init__ (self) :
		self.event_name = "N/A"
		self.date = "N/A"
		self.time = "N/A"
		self.place = "N/A"
		self.host = "N/A"

	# Event Name methods

	def set_event_name (self, ename) :
		self.event_name = ename
		print "Event Name set"

	def get_event_name (self) :
		return self.event_name

	#event date methods

	def set_date (self, date) :
		self.date = date
		print "Date set"

	def get_date (self) :
		return self.date

	# event time methods

	def set_time (self, time) :
		self.time = time
		print "Time set"

	def get_time (self) :
		return self.time

	# event place methods

	def set_place (self, place) :
		self.place = place
		print "Place set"

	def get_place (self) :
		return self.place

	# event host methods

	def set_host (self, host) :
		self.host = host
		print "Host set"

	def get_host (self) :
		return self.host

	# writing method
	def write_to_event (self)  :
		f = open('event.txt', 'w')
		f.write ("%s\n%s\n%s\n%s\n%s\n" %(self.get_event_name(), self.get_date(), self.get_time(), self.get_place(), self.get_host()))
		f.close()
