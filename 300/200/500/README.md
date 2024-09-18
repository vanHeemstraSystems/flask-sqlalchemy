# 500 - Displaying All Records

In this step, you’ll create a route and a template to display all the students in the database on the index page.

Leave the Flask shell running and open a new terminal window.

Open your ```app.py``` file to add a route for the index page to it:

```python title="app.py"
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)
```
app/app.py

Save and close the file.

Here, you create an ```index()``` view function using the ```app.route()``` decorator. In this function, you query the database and get all the students using the ```Student``` model with the ```query``` attribute, which allows you to retrieve one or more items from the database using different methods. You use the ```all()``` method to get all student entries in the database. You store the query result in a variable called ```students``` and pass it to a template called ```index.html``` that you render using the ```render_template()``` helper function.

Before you create the ```index.html``` template file on which you’ll display the existing students in the database, you’ll first create a base template, which will have all the basic HTML code other templates will also use to avoid code repetition. Then you’ll create the ```index.html``` template file you rendered in your index() function. To learn more about templates, see [How to Use Templates in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application).

Create a ```templates``` directory, then open a new template called ```base.html```:

```
$ cd app
$ mkdir templates
$ nano templates/base.html
```

Add the following code inside the ```base.html``` file:

```html title="base.html"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %} {% endblock %} - FlaskApp</title>
    <style>
        .title {
            margin: 5px;
        }

        .content {
            margin: 5px;
            width: 100%;
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
        }

        .student {
            flex: 20%;
            padding: 10px;
            margin: 5px;
            background-color: #f3f3f3;
            inline-size: 100%;
        }

        .bio {
            padding: 10px;
            margin: 5px;
            background-color: #ffffff;
            color: #004835;
        }

        .name a {
            color: #00a36f;
            text-decoration: none;
        }

        nav a {
            color: #d64161;
            font-size: 3em;
            margin-left: 50px;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">FlaskApp</a>
        <a href="#">Create</a>
        <a href="#">About</a>
    </nav>
    <hr>
    <div class="content">
        {% block content %} {% endblock %}
    </div>
</body>
</html>
```
app/templates/base.html

Save and close the file.

This base template has all the HTML boilerplate you’ll need to reuse in your other templates. The ```title``` block will be replaced to set a title for each page, and the ```content``` block will be replaced with the content of each page. The navigation bar has three links: one for the index page, which links to the ```index()``` view function using the ```url_for()``` helper function, one for a **Create** page, and one for an **About** page if you choose to add one to your application. You’ll edit this file later after you add a page for creating new students to make the **Create** link functional.

Next, open a new ```index.html``` template file. This is the template you referenced in the ```app.py``` file:

```
$ cd app
nano templates/index.html
```
Add the following code to it:

```html title="index.html"
{% extends 'base.html' %}

{% block content %}
    <h1 class="title">{% block title %} Students {% endblock %}</h1>
    <div class="content">
        {% for student in students %}
            <div class="student">
                <p><b>#{{ student.id }}</b></p>
                <b>
                    <p class="name">{{ student.firstname }} {{ student.lastname }}</p>
                </b>
                <p>{{ student.email }}</p>
                <p>{{ student.age }} years old.</p>
                <p>Joined: {{ student.created_at }}</p>
                <div class="bio">
                    <h4>Bio</h4>
                    <p>{{ student.bio }}</p>
                </div>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```
app/templates/index.html

Save and close the file.

Here, you extend the base template and replace the contents of the content block. You use an ```<h1>``` heading that also serves as a title. You use a [Jinja ```for``` loop](https://jinja.palletsprojects.com/en/3.0.x/templates/#for) in the line ```{% for student in students %}``` to go through each student in the ```students``` variable that you passed from the ```index()``` view function to this template. You display the student ID, their first and last name, email, age, the date at which they were added to the database, and their bio.

While in your ```flask_app``` directory with your virtual environment activated, tell Flask about the application (```app.py``` in this case) using the ```FLASK_APP``` environment variable. Then set the ```FLASK_ENV``` environment variable to ```development``` to run the application in development mode and get access to the debugger. For more information about the Flask debugger, see [How To Handle Errors in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-handle-errors-in-a-flask-application). Use the following commands to do this:

```
(.venv) gitpod /workspace/flask-sqlalchemy/app (main) $ export FLASK_APP=app
(.venv) gitpod /workspace/flask-sqlalchemy/app (main) $ export FLASK_ENV=development
```

Next, run the application:

```
(.venv) gitpod /workspace/flask-sqlalchemy/app (main) $ flask run
```

With the development server running, visit the following URL using your browser:

```
http://127.0.0.1:5000/
```

You’ll see the students you added to the database in a page similar to the following:

![image](https://github.com/user-attachments/assets/b8311d3a-4f93-4fbf-9b8b-3f2babab747d)

You’ve displayed the students you have in your database on the index page. Next, you’ll create a route for a student page, where you can display the details of each individual student.