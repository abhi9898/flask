from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'nickname': 'Abhi'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'Shashank'}, 
            'body': 'We have to work hard' 
        },
        { 
            'author': {'nickname': 'Abhi'}, 
            'body': 'We have to work really hard' 
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)