# Import `Flask` class
from flask import Flask, render_template, request

# Declare WSGI application i.e instance of `Flask` class
app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True

# `route()` decorator to tell Flask what URL should trigger our function
@app.route('/')
def index():
    return 'Home Page'

@app.route('/hola')
def hola():
    return 'Hola'

@app.route('/user/<username>')
def get_user_details(username):
    app.logger.debug('`username` argument.')
    return 'Your username is %s.' % username

@app.route('/user/<int:user_id>')
def get_user_details_meta(user_id):
    app.logger.debug('`user_id` argument.')
    return 'Your user Id is %d.' % user_id

@app.route('/post/<int:post_id>')
def get_post_details(post_id):
    return 'Post Id is %d.' % post_id

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404', 404

@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404'

@app.errorhandler(500)
def internal_server_error(e):
    return 'Error 500', 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.form['username']

    error = 'Invalid username/password'
    # Show the login page with form
    # return render_template('Template', error=error)
    return error

if __name__ == '__main__':
    app.run()
