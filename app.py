#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
   data = json.loads(request.data)
   print "New commit by: {}".format(data['commits'][0]['author']['name'])
   return "OK"


if __name__ == '__main__':
    print("Starting app on port %d" % (port))
    app.run()
