#!/usr/bin/python

# System imports
import json
import sys
import os.path

# API imports
from flask import Flask

# Business imports
from lib.core.methods import *
from lib.core.search import Search

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, welcome to the vFeed API"

@app.route('/vfeed/api/cve/<cve_id>', methods=['GET'])
def get_cve_detail(cve_id):
    return CveInfo(cve_id).get_cve()

@app.route('/vfeed/api/cpe/<cpe_id>', methods=['GET'])
def get_cpe(cpe):
    return Search(cpe).cpe()

if __name__ == '__main__':
    app.run(debug=True)

