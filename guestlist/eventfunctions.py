class Guest :

	# class includes all functions pertaining to adding a guest to a guest list
	# and adding the information for a guest

	def __init__ (self) :
		self.first_name = "N/A" 
		self.last_name = "N/A"

	def set_first (self, input_first) :
		s = input_first
		input_first_clean = s[0].capitalize() + s[1:]
		self.first_name = input_first_clean
		print "First set"

	def get_first (self) :
		return self.first_name

	def set_last (self, input_last) :
		s = input_last
		input_last_clean = s[0].capitalize() + s[1:]
		self.last_name = input_last_clean
		print "Last set"

	def get_last (self) :
		return self.last_name

	def write_to_guestlist (self) :
		f = open('guestlist.txt', 'a')
		f.write ("%s %s\n" %(self.get_first(), self.get_last()))
		f.close()
