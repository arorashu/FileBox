#winter training project
from flask import Flask, render_template, json, request
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from flask_admin import Admin, BaseView, expose
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
path = op.join(op.dirname(__file__),'static')

mysql = MySQL()
app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'jay'
app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
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

admin.add_view(FileAdmin(path+'/images/')) 

@app.route('/showSignUp')
def showSignUp():
	return render_template('signup.html')

@app.route('/signUp',methods=['POST','GET'])
def signUp():
	try:
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']

		# validate the received values
		if _name and _email and _password:

			# All Good, let's call MySQL

			conn = mysql.connect()
			cursor = conn.cursor()
			_hashed_password = generate_password_hash(_password)
			cursor.callproc('sp_createUser',(_name,_email,_hashed_password))
			data = cursor.fetchall()

			if len(data) is 0:
				conn.commit()
				return json.dumps({'message':'User created successfully !'})
			else:
				return json.dumps({'error':str(data[0])})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})

	except Exception as e:
		return json.dumps({'error':str(e)})
	finally:
		cursor.close()
		conn.close()

if __name__ == "__main__":
	app.run(port=5002)
