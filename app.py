from flask import Flask,render_template,request,redirect,url_for
from models import *

app=Flask(__name__)

@app.route('/')
def index():
    students=Student.select()
    return render_template('index.html',students=students)


@app.route('/create',methods=['POST','GET'])
def create():
    if request.method == 'POST':
        n=request.form['name']
        a=request.form['age']
        Student.create(name=n,age=a)
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/details/<int:id>')
def details(id):
    s=Student.get_by_id(id)
    return render_template('details.html',s=s)

@app.route('/delete/<int:id>')
def delete(id):
    s=Student.get_by_id(id)
    s.delete_instance()
    return redirect(url_for('index'))

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    s=Student.get_by_id(id)
    if request.method=='POST':
        s.age=request.form['age']
        s.name=request.form['name']
        s.save()
        return redirect(url_for('index'))
    else:
        return render_template('update.html',s=s)


if __name__=='__main__':
    app.run(debug=True)