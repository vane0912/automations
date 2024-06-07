from automations import create_app
from flask import render_template
app = create_app()

@app.route('/')
def homepage():
    return render_template('homepage.html')