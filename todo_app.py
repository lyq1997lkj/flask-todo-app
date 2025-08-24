    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('index', task_id=task_id))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task_post(task_id):
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for('index', task_id=task_id))

@app.route('/index')
def index():
    return render_template('index.html', tasks=tasks, task_id=task_id)

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete_task_get(task_id):
    return redirect(url_for('index', task_id=task_id))

if __name__ == '__main__':
    app.run(debug=True)