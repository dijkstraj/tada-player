from flask import Flask, jsonify
from subprocess import call
from os import listdir
from os.path import isfile, join
from fnmatch import fnmatch

app = Flask(__name__)

@app.route('/ping')
def ping():
  return 'pong'

@app.route('/list')
def list():
  sounds = [ f for f in listdir('.') if isfile(join('.', f)) and fnmatch(f, '*.wav') ]
  return jsonify(sounds=sounds)

@app.route('/play/<name>', methods=['GET', 'POST'])
def play(name):
  call(['aplay', name])
  return 'played ' + name

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0')