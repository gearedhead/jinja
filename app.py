from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.secret_key = "super secret key"


username='root'
password ='db123'
userpass='mysql+pymysql://' + username + ':' + password + '@'

server ='127.0.0.1'
dbname ='/fenix'

app.config['SQLALCHEMY_DATABASE_URI']= userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)

class Luker(db.Model):
    __tablename__='luker'
    id = db.Column(db.Integer, primary_key=True)
    call_number = db.Column(db.Integer, unique=True, nullable=False)
    item_type = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, nullable=False)
    work = db.Column(db.String, nullable=False)
    reported_date = db.Column(db.DateTime, nullable=False)
    attended_date = db.Column(db.DateTime, nullable=False)
    remarks = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    closed_date = db.Column(db.DateTime, nullable=False)

#def __init__(self, name, age, work, date):
  # # self.name = name
  # # self.age = age
  # # self.work = work
   ## self.date = date

@app.route('/')
def index():
    return render_template('index.html',data=Luker.query.all())

@app.route('/new', methods = ['GET','POST'])
def new():
     if request.method =='POST':
         if not request.form['call_number'] or not request.form['item_type'] or not request.form['description'] or not request.form['address'] or not request.form['mobile'] or not request.form['work'] or not request.form['reported_date'] or not request.form['attended_date'] or not request.form['remarks'] or not request.form['status'] or not request.form['closed_date']:
             flash('Please enter all the fields','error')
         else:
             data=Luker(call_number=request.form['call_number'],item_type=request.form['item_type'],description=request.form['description'],address=request.form['address'],mobile=request.form['mobile'],work=request.form['work'],reported_date=request.form['reported_date'],attended_date=request.form['attended_date'],remarks=request.form['remarks'],status=request.form['status'],closed_date=request.form['closed_date'])

             db.session.add(data)
             db.session.commit()
             
             flash('Records were successfully added')
             return redirect(url_for('index'))
     return render_template('new.html')

@app.route('/view', methods =['GET','POST'])
def view():
    if request.method=='POST':
        status_type=request.form['status']
        data=Luker.query.filter(Luker.status==status_type)
        return render_template('view.html',data=data)
    else:
     return render_template('view.html',data=Luker.query.all())

@app.route('/update',methods=['GET','POST'])
def update():
     if request.method=='POST':
      id=request.form['id']
      return 'hello'









if __name__=='__main__':
    app.run(debug=True)


