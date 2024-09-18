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



MORE