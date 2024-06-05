from automations import app
from flask import render_template

@app.route('/weekly')
def weekly():
    return render_template('weekly.html')