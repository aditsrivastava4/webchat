import MySQLdb
import sys
from datetime import datetime

	

def createDB():
	"""
	It will create the the new database 'ChatDB'.
	"""
	db = MySQLdb.connect("localhost","root","adit")
	# prepare a cursor object using cursor() method
	new_cursor = db.cursor()
	# execute SQL query using execute() method.
	new_cursor.execute("CREATE DATABASE ChatDB")
	#new_cursor.execute("CREATE TABLE CHAT(msg TEXT,ctime time)")
	db.close()
	create_table()


def create_table():
	"""
	It will create the the new table 'CHAT' in the 'ChatDB'.
	"""
	db = MySQLdb.connect("localhost","root","adit","ChatDB")
	# prepare a cursor object using cursor() method
	new_cursor = db.cursor()
	# execute SQL query using execute() method.
	new_cursor.execute("CREATE TABLE CHAT(msg TEXT,ctime DATETIME)")
	db.close()

def getData():
	"""
	It will get all the data from 'ChatDB'.
	"""
	db = MySQLdb.connect("localhost","root","adit","ChatDB")
	# prepare a cursor object using cursor() method
	new_cursor = db.cursor()
	

	try:
		# execute SQL query using execute() method.
		new_cursor.execute("SELECT * FROM CHAT")
	except MySQLdb.ProgrammingError:
		#if the table does not exist.
		create_table()
		return False

	data = new_cursor.fetchall();
	for d in data:
		print(d)
	db.close()
	return True

def inputData(input_data):
	"""
	Input the new data in the table 'CHAT'.
	"""
	if input_data=='':
		return
	db = MySQLdb.connect("localhost","root","adit","ChatDB")
	# prepare a cursor object using cursor() method
	new_cursor = db.cursor()
	# execute SQL query using execute() method.
	ctime = (str)(datetime.now())
	query = """insert into CHAT value("{msg}\","{t}")"""
	
	if (not sanitizeInputData(input_data)):
		return "Wrong Input"

	try:
		new_cursor.execute(query.format(msg = input_data,t = ctime))
	except MySQLdb.ProgrammingError:
		#if the table does not exist.
		create_table()
		return False
	db.commit()
	db.close()
	return True

def sanitizeInputData(msg):
	"""
	Sanitizing the MySQL Query.
	"""
	if ';' in msg or '--' in msg:
		try:
			raise InputError
		finally:
			print('Give proper input')
	return True


#this try check if the Database exist or not
try:	
	# Open database connection
	db = MySQLdb.connect("localhost","root","adit","ChatDB")
	db.close()
except MySQLdb.OperationalError:
	#Create the new Database 'ChatDB'.
	createDB()