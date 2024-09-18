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


MORE