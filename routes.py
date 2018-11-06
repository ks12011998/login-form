from flask import *
from functools import wraps
from login_form import Verifier

student = Blueprint("student",__name__,template_folder="templates/student")

def login_required(f):
	@wraps(f)
	def decorated_function(*args,**kwargs):
		if session.get('username',None) != None and session.get('username',"admin") != "admin":
			return f(*args,**kwargs)
		else:
			return redirect(url_for('main.login_page', next=request.url))
	return decorated_function


@student.route("/register/1")
def register_student_step_1():
	return render_template('register_1.html',title="Register | Step 1")


@student.route("/register/2")
def register_student_step_2():
	return render_template('register_2.html',title="Register | Step 2")


@student.route("/register/3")
def register_student_step_3():
	return render_template('register_3.html',title="Register | Final")


@student.route("/studentlogin",methods=['POST'])
def student_login():
	V = Verifier(request.form.get('id'),request.form.get('passwd'),"student")

	if V.verify():
		session['username'] = request.form.get('id')
		session['password'] = request.form.get('passwd')
		return redirect(url_for('student.student_home',id=request.form.get('id').upper()))
	else:
		flash("student")
		session['error'] = True
		return redirect(url_for('main.login_page',s='1'))


############################### Home pages ##########################

@student.route("/jee/student/<string:id>",methods=['GET','POST'])
@login_required
def student_home(id):
	return "Student with id "+session['username']+" has been successfully logged in"


