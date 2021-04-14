from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user  = {'username':'Miguel'}
    posts = [
        {
            'author':{'username':'John'},
            'body':'A story about penguins'
        },
        {
            'author':{'username':'Anla'},
            'body':'Once upon a time in the bleast'
        }
    ]
    return render_template('index.html', title='Home',user = user, posts = posts)