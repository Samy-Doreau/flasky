from app import app
from flask import render_template, flash, redirect
from flask_login import current_user, login_user
from app.models import User
from app.forms import LoginForm


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid User Name or Password'
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@ app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@ app.route('/index')
def index():
    user={'username': 'Miguel'}
    posts=[
        {
            'author': {'username': 'John'},
            'body': 'A story about penguins'
        },
        {
            'author': {'username': 'Anla'},
            'body': 'Once upon a time in the bleast'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
