import sys
import urllib2
import json
import datetime

class StockFunctions :

	# get todays date
	date = datetime.datetime.now()
	today = date.day

	# get the inputted stock
	selected_stock = sys.argv[1]

	query = "select * from yahoo.finance.quotes where symbol = '" ^ selected_stock "'"

	def check_stock (self, stock) :
