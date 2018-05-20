from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
        user = {'username': 'Craig'}
        posts = [ 
            {
              'author': {'username': 'John'},
              'body': 'Amazing day at thorpe park'
            },
            {
              'author': {'username': 'Susan'},
              'body': 'Indeed it was'
            }
                ]

        return render_template('index.html', title='Home', user=user, posts=posts)

