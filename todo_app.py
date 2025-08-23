from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for tasks
tasks = []

# HTML template embedded in the Python file
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .add-task-form {
            margin-bottom: 30px;
            display: flex;
            gap: 10px;
        }
        input[type="text"] {
            flex: 1;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .delete-btn {
            background-color: #dc3545;
            padding: 5px 10px;
            font-size: 14px;
        }
        .delete-btn:hover {
            background-color: #c82333;
        }
        .task-list {
            list-style: none;
            padding: 0;
        }
        .task-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px;
            margin-bottom: 10px;
            background-color: #f8f9fa;
            border-radius: 5px;
            border-left: 4px solid #007bff;
        }
        .task-text {
            flex: 1;
            font-size: 16px;
        }
        .no-tasks {
            text-align: center;
            color: #666;
            font-style: italic;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>My To-Do List</h1>
        
        <!-- Add new task form -->
        <form method="POST" action="{{ url_for('add_task') }}" class="add-task-form">
            <input type="text" name="task" placeholder="Enter a new task..." required>
            <button type="submit">Add Task</button>
        </form>
        
        <!-- Task list -->
        {% if tasks %}
            <ul class="task-list">
                {% for i in range(tasks|length) %}
                <li class="task-item">
                    <span class="task-text">{{ tasks[i] }}</span>
                    <form method="POST" action="{{ url_for('delete_task', task_id=i) }}" style="display: inline;">
                        <button type="submit" class="delete-btn">Delete</button>
                    </form>
                </li>
                {% endfor %}
            </ul>
        {% else %}
            <div class="no-tasks">No tasks yet. Add one above!</div>
        {% endif %}
        
        <div style="margin-top: 30px; text-align: center; color: #666;">
            Total tasks: {{ tasks|length }}
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    """Display the main page with all tasks"""
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task to the list"""
    task = request.form.get('task')
    if task and task.strip():
        tasks.append(task.strip())
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task from the list - INTENTIONAL BUG: Always deletes the last task"""
    if tasks:
        # BUG: Instead of deleting the task at task_id, always delete the last task
        tasks.pop()  # This should be: tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Add some sample tasks for demonstration
    tasks.extend([
        "Buy groceries",
        "Walk the dog",
        "Finish project report"
    ])
    
    print("Starting Flask To-Do List application...")
    print("Visit http://127.0.0.1:5000 in your browser")
    app.run(debug=True, host='127.0.0.1', port=5000)