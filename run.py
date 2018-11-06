from flask import Flask
from admin.routes import admin
from student.routes import student
from main.routes import main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nilekrator'

app.register_blueprint(admin)
app.register_blueprint(student)
app.register_blueprint(main)

if __name__ == '__main__':
	app.run(debug=True,port=80)
