import os
from urllib import parse
import psycopg2
from datetime import datetime


def connectDB(query,setectQ=0):
	'''parse.uses_netloc.append("postgres")
	url = parse.urlparse(os.environ["DATABASE_URL"])

	conn = psycopg2.connect(
	    database=url.path[1:],
	    user=url.username,
	    password=url.password,
	    host=url.hostname,
	    port=url.port
	)'''
	conn = psycopg2.connect(
		database='webchatDB',
		user='adit',
		password='adit'
	)
	conn.autocommit = True
	cur = conn.cursor()
	cur.execute(query)
	if setectQ==1:
		return cur
	cur.close()

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

def create_table():
	"""
	It will create the the new table 'CHAT' in the 'ChatDB'.
	"""
	connectDB("""CREATE TABLE CHAT(msg TEXT,ctime TIMESTAMP)""")

def getData():
	"""
	It will get all the data from 'ChatDB'.
	"""
	query = """SELECT * FROM CHAT"""
	try:
		cur = connectDB(query,1)
	except:
		create_table()
		cur = connectDB(query,1)
	data = cur.fetchall()
	cur.close()
	return data

def inputData(input_data):
	"""
	Input the new data in the table 'CHAT'.
	"""
	if input_data=='':
		return
	# execute SQL query using execute() method.
	ctime = (str)(datetime.now())
	ctime = ctime[:19]
	query = """insert into CHAT values('{msg}','{t}')"""

	if (not sanitizeInputData(input_data)):
		return False
	try:
		connectDB(query.format(msg = input_data,t = ctime))
	except :
		try:
			create_table()
		finally:
			connectDB(query.format(msg = input_data,t = ctime))
	return True

