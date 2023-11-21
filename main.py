from flask import Flask,render_template,request,redirect,url_for 
import pymysql

app=Flask(__name__)
app.secret_key='helloworld'
#Configure mysql
db=pymysql.connect(host='localhost',user='root',password='',database='todo_app')
cursor=db.cursor()

@app.route('/')
def index():
    cursor.execute('SELECT * FROM tasks')
    tasks=cursor.fetchall()
    return render_template('index.html',tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task=request.form.get('task')
    cursor.execute('INSERT INTO tasks (content) VALUES (%s)', (task,))
    db.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    cursor.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    db.commit()
    return redirect(url_for('index'))

if __name__=='__main__':
	app.run(debug=True)
    