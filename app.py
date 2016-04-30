#winter training project
from flask import Flask, render_template
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
	#temporary
	return render_template('register.html')


@app.route("/login")
def get_login():
	return render_template('login.html')


admin.add_view(FileAdmin(path+'/files/' , name='Files'))  

if __name__ == '__main__':
	app.run()
