from automations import create_app
from flask import render_template
app = create_app()
@app.route('/weekly')
def weekly():
    return render_template('weekly.html')