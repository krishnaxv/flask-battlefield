# Flask

### Introduction

> Flask is a micro framework for Python based on Werkzeug, Jinja 2 and good intentions.

**Simple Flask Application**

```python
# Import `Flask` class
from flask import Flask

# Instance of `Flask` class
app = Flask(__name__)

# `route()` decorator to tell Flask what URL should trigger our function
@app.route('/')
def index():
  return 'Hola!'

if __name__ == '__main__':
  app.run()
```

**How to run the application?**

Run command `python app.py`. This will launch a simple built-in server, which is good enough for testing.

`Note` Do not name your application *flask.py* because this would conflict with **Flask** itself.

### Routing

> ***Routing*** refers to the definition of application end points (URLs) and how they respond to client requests.

The `route()` decorator is used to bind a function to a URL.

**Examples**

```python
@app.route('/')
def index():
  return 'Home Page'

@app.route('/hola')
def hola():
  return 'Hola'
```

### Variable Rules

You can add variable parts to a URL with `<variable_name>`. This `<variable_name>` is passed as keyword argument to the function.

You can also use a converter that can be used by specifying a rule with `<converter:variable_name>`.

```python
@app.route('/user/<username>')
def get_user_details(username):
  return 'Your username is %s.' % username

@app.route('/post/<int:post_id>')
def get_post_details(post_id):
  return 'Post Id is %d.' % post_id
```

**Converters**

### HTTP Methods

Different methods can be used for accessing URLs.

*By default, a route only answers to GET requests*, but that can be changed by providing the methods argument to the `route()` decorator.

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    # Process the parameters
  else:
    # Show the login page with form
```

`Flask Documentation` **What different HTTP methods are available?**

`GET`
This is the most common method. The browser tells the server to just get the information stored on that page and return it.

`HEAD`
The browser tells the server to get the information, but it is only interested in the headers, not the content of the page.

`POST`
The browser tells the server that it wants to post some new information to that URL and that the server must ensure the data is stored and only stored once. This is how HTML forms usually transmit data to the server.

`PUT`
Similar to `POST` but the server might trigger the store procedure multiple times by overwriting the old values more than once.

`DELETE`
Remove the information at the given location.

`OPTIONS`
Provides a quick way for a client to figure out which methods are supported by this URL.

### Rendering Templates

*What are templates?*

*Why do we need templates?*

Flask internally uses `Jinja2` template engine.

Example template

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Flask Template</title>
  </head>
  <body>
  {% if name %}
    <h1>Hello {{ name }}!</h1>
  {% else %}
    <h1>Hola!</h1>
  {% endif %}
  </body>
</html>
```

### Accessing Request Data

For web applications it’s crucial to react to the data a client sends to the server. In Flask this information is provided by the global `request` object.

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if check_login(request.form['username'], request.form['password']):
      return valid_user(request.form['username'])
    else:
      error = 'Invalid username/password'
  # Show the login page with form
  return render_template('login.html', error=error)
```

If key doesn't exist in the form attribute, a special KeyError is raised. You can catch it like a standard KeyError but if you don’t do that, a HTTP 400 Bad Request error page is shown instead.

To access parameters submitted in the URL (?key=value) you can use the args attribute:

```python
search_query = request.args.get('key', '')
```

### Redirects & Errors

To redirect a user to another endpoint, use the redirect() function; to abort a request early with an error code, use the abort() function.

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
  return redirect(url_for('login'))

@app.route('/login')
def login():
  # Access denied
  abort(401)
  this_is_never_executed()
```

By default a black and white error page is shown for each error code. If you want to customize the error page, you can use the errorhandler() decorator.

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
  return render_template('page_not_found.html'), 404
```

### Sessions

session which allows you to store information specific to a user from one request to the next.

In order to use sessions you have to set a secret key.

```python
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
  if 'username' in session:
    return 'Logged in as %s' % session['username']
  return 'You are not logged in.'

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['username'] = request.form['username']
    return redirect(url_for('index'))
  return '''
    <form action="" method="post">
      <p><input type="text" name="username">
      <p><input type="submit" value="Login">
    </form>
  '''

@app.route('/logout')
def logout():
  # Remove the username from the session if it's there
  session.pop('username', None)
  return redirect(url_for('index'))

# Secret key
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
```

### Logging

Example

```python
app.logger.debug('Debugging')
app.logger.warning('Warning')
app.logger.error('Error')
```
