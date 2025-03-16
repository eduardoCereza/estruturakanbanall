from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    tasks = {
        "To Do": ["Task 1", "Task 2"],
        "In Progress": ["Task 3"],
        "Done": ["Task 4"]
    }
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
