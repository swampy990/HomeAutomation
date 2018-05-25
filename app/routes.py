from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from app.forms import CarForm

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


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)

@app.route('/miles', methods=['GET','POST'])
def mileage():
    form = CarForm()
    return render_template('miles.html', title='Mileage Tracker', form=form)
