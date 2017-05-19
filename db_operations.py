import sqlite3

class Db_Operations():

	def __init__(self,dbname):
		self.dbname=dbname

	def get_connection(self):
		try:
		  conn=sqlite3.connect(self.dbname)
		  cur=conn.cursor()
		  return conn,cur
		except Exception as err:
			print err

	def create_table(self,query):
		try:
			conn,cur=self.get_connection()
			cur.execute(query)
			conn.commit()
			conn.close()
		except Exception as err:
			print err

	def insert_values_table(self,query,list2):
		conn,cur=self.get_connection()
		try:
			for a in list2:
				cur.execute(query,a)
			conn.commit()
			conn.close()
		except Exception as err:
			print err

	def delete_values_table(self,query):
		conn,cur=self.get_connection()
		try:
			cur.execute(query)
			conn.commit()
			conn.close()
		except Exception as err:
			print err    

	def update_values_table(self,query):
		conn,cur=self.get_connection()
		try:
		   cur.execute(query)
		   conn.commit()
		   conn.close()
		except Exception as err:
		   print err
						




			
					
 


			



			
				
		
		
		
			
	