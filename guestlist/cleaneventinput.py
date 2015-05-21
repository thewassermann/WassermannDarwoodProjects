import sys

class EventInput :

	# event name 
	def clean_event_name (self, ename) :
		s = ename
		return s[0].capitalize() + s[1:]	

	# date (will be dealt with be interface)

	# time (will be dealt with by interface)

	# place
	def clean_place (self, place) :
		s = place
		return s[0].capitalize() + s[1:]	

	# host 
	def clean_name (self, first, last) :
		sf = first
		sl = last
		return sf[0].capitalize() + sf[1:] + " " + sl[0].capitalize() + sl[1:]

