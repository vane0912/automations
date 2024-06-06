from flask import Flask
app = Flask(__name__)

import automations.homepage
import automations.weekly
import automations.applications
