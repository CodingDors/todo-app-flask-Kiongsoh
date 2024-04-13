from flask import Flask, render_template, request, redirect

app = Flask(__name__)

todo = []

@app.route("/", methods=["GET", "POST"])
def index():
  """ 
  Handle GET Requests in index Function:
    Add a conditional check for the request method.
    If the method is "GET", use render_template to render "index.html" and pass the todo list as a variable.
  """
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
  # TODO
  return redirect("/")
