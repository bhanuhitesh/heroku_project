from flask import Flask
app = Flask(..name..)

@app.route('/')
def index():
  return 'hello world'
