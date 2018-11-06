import pymysql as mysql

class Verifier:
	def __init__(self,ID,passwd,Type):
		self.id = ID.upper()
		self.passwd = passwd
		self.type = Type
		self.conn = self.connection()

	def connection(self,host="localhost",user="root",password=""):
		conn = mysql.connect(host,user,password,db="jee")
		return conn

	def verify(self):
		cursor = self.conn.cursor()
		if self.type == "student":
			cursor.execute("SELECT ID,password FROM credential WHERE ID='%s' AND password='%s'"%(self.id,self.passwd))
			result = cursor.fetchall()

			#student credentials are wrong
			if not result:
				return None
			else:
				return result[0][0],result[0][1]			# student credentials

		elif self.type == "admin":
			cursor.execute("SELECT ID,password FROM credential WHERE ID='%s' and password='%s'"%("admin",self.passwd))
			result = cursor.fetchall()
			#admin password is wrong
			if not result:
				return None
			else:
				return result[0][0],result[0][1]			# admin credentials
