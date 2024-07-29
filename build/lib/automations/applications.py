from .automations_list import automations_list_applications
from automations import app
from flask import render_template

@app.route('/applications')
@app.route('/applications/<app_type>')
def runapp(app_type=None):
    test = ["India", "Turkey", "Egypt"]
    filtered_Array = []
    for x in automations_list_applications:
        if x['Country'] == app_type:
            filtered_Array.append(x)
    return render_template('applications.html', categories=test, app_type=app_type, automations=filtered_Array)

@app.post('/test')
def testrun():
    
    return 'this worked'