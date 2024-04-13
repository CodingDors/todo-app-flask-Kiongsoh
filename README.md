# ToDo App Exercise - Flask
Welcome to the ToDo App Exercise with Flask! In this assignment, you'll be creating a basic ToDo application using Flask.

You'll write only in `app.py`, the other files are done for you. If you want to see the solution, check the `the_answer.py` file.

## 🎯 Objective:
Your task is to create a simple ToDo application that allows a user to:

1. Enter a task using a form.
2. View the tasks they've added to a global list that gets updated with each new entry.
3. Remove the task they want to delete (by clicking in a individual button for each item)

## 📚 Starter Code
The HTML code consists of two primary components:

1. **Task Display List**
   - **List Container**: Uses a `<ul>` element to create an unordered list. Each task in the application is represented as an individual list item (`<li>`) within this container.
   - **Dynamic Task Listing**: The `{% for task in todo %}` loop dynamically populates the list with tasks. For each task, it creates a list item (`<li>`) displaying the task content.
   - **Remove Button**: Each task has an associated form with a "Remove" button. This form submits a POST request to the `/remove` route, indicating the task to be removed. The task to be removed is passed as a hidden field in the form.

2. **Task Input Form**
   - **Form Element**: A separate `<form>` tag at the bottom of the page, designated for adding new tasks. This form submits to the root route (`"/"`) as a POST request.
   - **Task Input Field**: An `<input>` element of the type text, allowing users to input a new task. It includes a placeholder text "Add Task" to guide users.
   - **Submit Button**: A submit button within the form, enabling users to submit the new task. Upon submission, the task is sent to the server and is expected to be added to the task list.

## ✅ Specific Tasks:
In app.py, set up Flask routes to handle:
1. **Handle GET Requests in index Function:**
  - Inside the index function, add a conditional check for the request method.
  - If the method is `"GET"`, use `render_template` to render `"index.html"` and pass the `todo` list as a variable.

2. **Handle POST Requests in index Function for Adding Tasks:**
  - Still in the index function, add an `else` block to handle `POST` requests.
  - Retrieve the task from the form data using `request.form.get("task")`.
  - Append the retrieved task to the `todo` list.
  - Finally, redirect the user back to the home page using `return redirect("/")`.

3. **Handle POST Requests in remove Function:**
  - In the remove function, add code to handle `POST` requests.
  - Retrieve the task to be removed from the form data using `request.form.get("task")`.
  - Remove the specified task from the todo list using `todo.remove(task)`.
  - Redirect the user back to the home page.

## 📘 How to Run Your Website:
1. Open your terminal
2. Run the command: `python -m flask run`
3. Access the application by navigating to `localhost:5000` in your web browser.

## 🚀 How to Run Tests:
1. Ensure your Flask server is not running (`ctrl` + `C`), or it will occupy the terminal.
2. In your terminal, run `python test_app.py`.

## 🤔 How to Submit:
Once all the tests have completed:

1. Stage Changes:
  - View your changes in the Source Control view.
  - Click on the + (plus) sign next to the files you wish to stage.
2. Commit Changes:
  - Enter a descriptive commit message.
  - Press Ctrl + Enter (or Cmd + Enter on macOS) to commit the changes.
3. Push Changes:
  - Click on the ellipsis ... in the Source Control view.
  - Select Push.
4.Verify you code has passed

## How the Project will Look Like
![Local Image](project.png)
