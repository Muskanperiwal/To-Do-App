from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    details = db.Column(db.String(500), nullable = False)
    Date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    
# def addTodo():
#     todo = Todo(title=title, details=details)
#     db.session.add(todo)
#     db.session.commit()
    
with app.app_context():
    db.create_all()
    
# def addTodo():
#     admin = Todo(
#             sno= 1,
#             title='admin@example.com',
#             details='Nitin'
#         )
#     db.session.add(admin)
#     db.session.commit()

    
# with app.app_context():
#         db.create_all()




@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        title = request.form['title']
        details = request.form['details']

        def addTodo():
            if (title=='' and details==''): return

            todo = Todo(title=title, details=details)
            db.session.add(todo)
            db.session.commit()
        addTodo()
    allTodo = Todo.query.all()
    # addTodo()
    return render_template('index.html', allTodo = allTodo)



@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/list')
def list():
    return render_template('list.html')


@app.route('/update/<int:sno>', methods = ['GET', 'POST'])
def update(sno):
    if request.method== 'POST':
        title = request.form['title']
        details = request.form['details']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.details = details
        db.session.add(todo)
        db.session.commit()
        return redirect('/home')

    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)
    # return 'This is my update page'

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/home")




if __name__ == '__main__':
    app.run(debug=True)