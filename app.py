#winter training project

import MySQLdb

from flask import Flask, render_template, request, json
from flask_admin import Admin, BaseView, expose
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
path = op.join(op.dirname(__file__),'static')

app = Flask(__name__)
admin = Admin(app, template_mode='bootstrap3')
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "asdasuhdasdasd"
class PageView(BaseView):
	def is_accessible (self):
		return True
	@expose('/')
	def index(self):
		return self.render('admin/index.html')





@app.route("/")
def main():
	return render_template('index.html')

@app.route("/register", methods=['GET'])
def get_register():
	return render_template('register.html')

@app.route("/register", methods=['POST'])
def post_register():
	#read the values posted by html form
	name = request.form['inputName']
	email = request.form['inputEmail']
	password = request.form['inputPassword']

	#validate the received values, i.e. check if they exist
	# if( name and email and password ):
	# 	return json.dumps({'status': 1})
	# else:
	# 	return json.dumps({'status': 0})

	#make connection to database
	db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="filebox")
	# you must create a Cursor object to let you execute queries
	cur = db.cursor()
	cur.execute("""INSERT INTO USERS (NAME, EMAIL, PASSWORD) VALUES (%s, %s, %s )""", (name, email, password) )
	
	# cur.execute("SELECT VERSION()")
	# # Fetch a single row using fetchone() method.
	# data = cur.fetchone()
	# print "Database version : %s " % data
	db.commit()
	cur.close()
	db.close()
	return render_template('home.html', name=name)

@app.route("/login")
def get_login():
	return render_template('login.html')


admin.add_view(FileAdmin(path+'/files/' , name='Files'))  

if __name__ == '__main__':
	app.run()
