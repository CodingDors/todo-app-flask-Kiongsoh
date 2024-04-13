from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", todo=todo)
    else:
        task = request.form.get("task")
        todo.append(task)
        return redirect("/")

@app.route("/remove", methods=["POST"])
def remove():
    if request.method == "POST":
      task = request.form.get("task")
      todo.remove(task)
      return redirect("/")
