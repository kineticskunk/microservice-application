from flask import Flask,render_template, redirect, url_for,request, jsonify, abort,request
from flask_sqlalchemy import SQLAlchemy
from form import StudentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable= False)
  physics = db.Column(db.Integer)
  maths = db.Column(db.Integer)
  chemistry = db.Column(db.Integer)

  def __repr__(self):
    return f"Student('{self.name}','{self.physics}','{self.maths}','{self.chemistry}')"


#curl -i http://127.0.0.1:5000/
# @app.route('/', methods=["GET"])
# def retreive_results():



  
#   data = Student.query.all()

#   output = []

#   for x in data:
#     student_data = {}
#     student_data['id'] = x.id
#     student_data['name'] = x.name
#     student_data['physics'] = x.physics
#     student_data['maths'] = x.maths
#     student_data['chemistry'] = x.chemistry
#     output.append(student_data)

#   return jsonify({'student': output})

#curl -i http://127.0.0.1:5000/results/<intID>
# @app.route('/results/<int:indexId>',methods=["GET"])
# def get_one_student(indexId):
#   student = Student.query.filter_by(id = indexId).first()

#   if not student:
#     return jsonify({'message':'No user found'})

#   student_data = {}
#   student_data['id'] = student.id
#   student_data['name'] = student.name
#   student_data['physics'] = student.physics
#   student_data['maths'] = student.maths
#   student_data['chemistry'] = student.chemistry

#   return jsonify({'student':student_data})

#curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"Sivu\",\"physics\":30,\"maths\":90,\"chemistry\":10}"" http://127.0.0.1:5000/results
@app.route('/', methods=['GET','POST'])
def add_results():
    form = StudentForm()
    if form.validate_on_submit():
      student = Student(name=form.name.data, physics=form.physics.data, maths=form.maths.data,chemistry=form.chemistry.data,)
      db.session.add(student)
      db.session.commit()
      return redirect(url_for('add_results'))
    else:
      return render_template('home.html', form=form)

@app.route('/results', methods=['GET','POST'])
def results():
  data = Student.query.all()
  return render_template('results.html', data = data)


  


#curl -i -H "Content-Type: application/json" -X PUT -d "{\"name\":\"Sivu\",\"physics\":10,\"maths\":40,\"chemistry\":30}" http://127.0.0.1:5000/results/<intID>
@app.route('/results/<int:student_id>')
def student(student_id):
  
  student = Student.query.get_or_404(student_id)

  return render_template('student.html', student=student)

@app.route('/results/<int:student_id>/update', methods=['GET','POST'])
def update_student(student_id):
    student = Student.query.get_or_404(student_id)
    form = StudentForm()
    if form.validate_on_submit():
        student.name = form.name.data 
        student.physics = form.physics.data  
        student.maths =  form.maths.data
        student.chemistry = form.chemistry.data          
        db.session.commit()
        return redirect(url_for('student', student_id=student.id))
    elif request.method == 'GET': 
         form.physics.data = student.name  
         form.physics.data = student.physics
         form.maths.data = student.maths
         form.chemistry.data = student.chemistry   
    return render_template('home.html', form=form)



@app.route("/results/<int:student_id>/delete", methods=['GET'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit() 
    return redirect(url_for('results'))       











#curl -i -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/results/<intID>
# @app.route('/results/<int:indexId>', methods=['DELETE'])
# def delete_student(indexId):

#   student = Student.query.filter_by(id = indexId).first()

#   if not student:
#     return jsonify({'message':'No user found'})

#   db.session.delete(student)
#   db.session.commit()

#   return jsonify({'message':'Student found and Deleted'})

if __name__ == '__main__':
 app.run(debug=True)
