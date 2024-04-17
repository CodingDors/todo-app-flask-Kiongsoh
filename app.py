from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo = ["Eat", "Sleep"]

@app.route("/", methods=["GET", "POST"])
def index():
  """ 
  Handle GET Requests in index Function:
    Add a conditional check for the request method.
    If the method is "GET", use render_template to render "index.html" and pass the todo list as a variable.
  """
  if request.method == "GET":
    return render_template("index.html", todo = todo)
  elif request.method == "POST":
    new_task = request.form.get("task")
    todo.append(new_task)
    return render_template("index.html", todo = todo)

  # TODO

  """
  Handle POST Requests in index Function for Adding Tasks:
    Still in the index function, add an else block to handle POST requests.
    Retrieve the task from the form data using request.form.get("task").
    Append the retrieved task to the todo list.
    Finally, redirect the user back to the home page using return redirect("/").
  """
  # TODO
  return render_template("index.html")


@app.route("/remove", methods=["POST"])
def remove():
  """
  Handle POST Requests in remove Function:
    In the remove function, add code to handle POST requests.
    Retrieve the task to be removed from the form data using request.form.get("task").
    Remove the specified task from the todo list using todo.remove(task).
    Redirect the user back to the home page.
  """
  task_del = request.form.get("task")
  todo.remove(task_del)

  # TODO
  return redirect("/")
