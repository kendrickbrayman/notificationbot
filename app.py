import os
import json
import defs

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request



app = Flask(__name__)

@app.route('/',methods=['POST'])

def webhook():
  data = request.get_json()
  if (data['text'].find("!") == 0):
    defs.parse_data(data)
  return "ok", 200

""" todo: 
-add compare function
"""