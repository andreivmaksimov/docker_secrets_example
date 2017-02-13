#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)
 
@app.route('/')
def index():
  try:
    db_password = None
    f = open('/run/secrets/db-password', 'r')
    db_password = f.readline()
  except IOError:
    pass
  finally:
    return render_template('index.html', password=db_password)
 
if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0')
