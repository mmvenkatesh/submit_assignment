import sqlite3

class Db_Operations():

	def __init__(self,dbname):
		self.dbname=dbname

	def create_database(self):
		try:
		  connection=sqlite3.connect(dbname)
		except Exception as err:
			print err

	def create_table(sef,query):
		try:
			connection=sqlite3.connect(dbname)
			cur=connection.execute(query)
			connection.commit()
			connection.close()
		except Exeception as err:
			print err

	#def insert_values_table(self,query,list2):
		#connection=sqlite3.connect(dbname)
		#try:
			#for a in list2:
				#cur=connection.execute(query,a)
			#connection.commit()
			#connection.close()
		#except Exception as err:
			#print err


			



			
				
		
		
		
			
	