from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Miguel'}
    
    # Seed data
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beatiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template(
        'index.html', 
        title="Home", 
        user=user, 
        posts = posts)