from flask import render_template
from app import app
from config import config
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
        runningConfig = config.Config
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

        return render_template('index.html', title='Home', user=user, posts=posts, secret_key = runningConfig.SECRET_KEY)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Sign In', form=form)

