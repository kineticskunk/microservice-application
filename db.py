from wsgi import db
from wsgi import Student
import os


db.create_all()

# Data to initialize database with
Data = [
	{'name'		: 'Darren'	,'physics': 1, 'maths': 1, 'chemistry':1},
	{'name'		: 'Kent'	,'physics': 1, 'maths': 1, 'chemistry':1},
	{'name'		: 'Bunny'	,'physics': 1, 'maths': 1, 'chemistry':1}
]

# Iterate over the PEOPLE structure and populate the database
for xData in Data:
	d = Student(name=xData['name'], physics=xData['physics'],maths=xData['maths'], chemistry=xData['chemistry'])
	db.session.add(d)

db.session.commit()